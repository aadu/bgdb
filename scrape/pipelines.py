

class DjangoItemPipeline:

    def process_item(self, item, spider):
        item.save()
        return item
