from collections import OrderedDict

from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from scrapy.item import Field, Item, ItemMeta


class DRFItemMeta(ItemMeta):
    def __new__(mcs, class_name, bases, attrs):
        _meta = attrs.pop('Meta')
        if _meta is None:
            raise ValueError("Must define Meta on DRFItem subclass")
        if hasattr(_meta, 'serializer'):
            serializer = _meta.serializer()
            only = getattr(_meta, 'fields', [])
            exclude = getattr(_meta, 'exclude', [])
            include = getattr(_meta, 'include', [])
            _model_fields = []
            for name, field in serializer.fields.items():
                is_not_in_only = only and name not in only
                is_excluded = name in exclude
                is_read_only = field.read_only and name not in include
                if is_not_in_only or is_excluded or is_read_only:
                    continue
                attrs[name] = Field()
                _model_fields.append(name)
            _meta.model_fields = _model_fields
        attrs['_meta'] = _meta
        cls = super().__new__(mcs, class_name, bases, attrs)
        cls.fields = cls.fields.copy()
        return cls


class DRFItem(Item, metaclass=DRFItemMeta):
    def save(self, commit=True, skip_errors=False):
        if not self.is_valid:
            if not skip_errors:
                msg = '\n'.join([f'{k}: {v}' for k, v in self.instance.errors.items()])
                raise ValidationError(f"{len(self.instance.errors)} errors found: {msg}")
        elif commit:
            self.instance.save()
        return self.instance

    @cached_property
    def is_valid(self, exclude=None):
        return self.instance.is_valid()

    @cached_property
    def errors(self):
        if not self.is_valid:
            return self.instance.errors
        return None

    @cached_property
    def model(self):
        return self._meta.serializer.Meta.model

    @cached_property
    def instance(self):
        data = dict((k, self.get(k)) for k in self._values if k in self._meta.model_fields)
        obj = None
        if 'id' in data:
            try:
                obj = self.model.objects.get(pk=data['id'])
            except self.model.DoesNotExist:
                pass
        return self._meta.serializer(data=data, instance=obj)

    class Meta:
        abstract = True
