import os

from django.core.files import File

class DjangoItemPipeline:

    def process_item(self, item, spider):
        if 'images' in item and item['images']:
            image = item['images'][0]
            item['image_url'] = image['url']
            image_path = os.path.join(spider.settings['IMAGES_STORE'], image['path'])
            with open(image_path, 'rb') as f:
                data = File(f, name=os.path.basename(image['path']))
                item['image'] = data
                item.save()
        else:
            item.save()
        return item
