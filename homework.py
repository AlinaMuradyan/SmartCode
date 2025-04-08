class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    def item_count(self):
        return len(self.collection)
    
    def page_count(self):
        division_result = len(self.collection) // self.items_per_page
        if len(self.collection) % self.items_per_page != 0:
            return division_result + 1
        return division_result

    def page_item_count(self, page_index):
        total = self.page_count()
        if page_index >= total or page_index < 0:
            return -1
        if page_index == total - 1:
            return len(self.collection) - self.items_per_page * (total - 1)
        return self.items_per_page
    
    def page_index(self, item_index):
        if item_index >= len(self.collection) or item_index < 0:
            return -1
        return item_index // self.items_per_page

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.page_count())
print(helper.item_count()) 
print(helper.page_item_count(0)) 
print(helper.page_item_count(1)) 
print(helper.page_item_count(2))
print(helper.page_index(5))
print(helper.page_index(2))
print(helper.page_index(20))
print(helper.page_index(-10))

