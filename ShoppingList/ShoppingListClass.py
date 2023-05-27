# https://www.youtube.com/watch?v=NUdLj27MVC8&list=PLTwy92rWKPiGDC_8v8L0vmCMwLd0a95u0&index=24

class ShoppingList:
    def __init__(self, list_name):
        self.items = []
        self.list_name = list_name
    
    def prnt_name(self):
        print([k for k,v in globals().items() if v is self])
        

    def add_item(self, item):
        if not (item in self.items):
            self.items.append(item)

    def remove_item(self, item) -> None:
        if item in self.items:
            self.items.remove(item)

    def get_list(self):
        return self.items

    def get_num_items(self):
        return len(self.items)

    def print_list(self):   # SPECIAL: for printing object PRETTY
        print(f"List Name: {self.list_name}\nItems: {self.items}\n")

    # def __str__(self):   # SPECIAL: for printing object PRETTY
    #     return f"List Name: {self.list_name} \nItems: {self.items}\n"
