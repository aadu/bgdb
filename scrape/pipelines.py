

class DjangoItemPipeline:

    def process_item(self, item, spider):
        # print(f"\n\n{item['id']}: {item['name']}\n")
        # item.save()
        return item
