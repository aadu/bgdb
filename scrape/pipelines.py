

class DjangoItemPipeline:

    def process_item(self, item, spider):
        # try:
        #     print(f"\n\n{item['id']}: {item['name']}\n")
        # except:
        #     pass
        # item.save()
        return item
