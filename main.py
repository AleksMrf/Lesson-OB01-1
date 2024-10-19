class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
           self.items[item_name] = new_price
           print(f"Цена товара '{item_name}' обновлена на {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def show_items(self):
        print(f"Товары в магазине '{self.name}':")
        for item, price in self.items.items():
            print(f"{item}: {price}")

store1 = Store("Магазин А", "Улица 1, 1")
store2 = Store("Магазин Б", "Улица 2, 2")
store3 = Store("Магазин В", "Улица 3, 3")

store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("молоко", 1.2)
store2.add_item("хлеб", 0.85)

store3.add_item("сок", 1.5)
store3.add_item("печенье", 2.0)


print("\nТестирование методов для 'Магазин А':")
store1.show_items()

store1.add_item("апельсины", 0.9)

store1.update_price("яблоки", 0.6)

store1.remove_item("бананы")

price = store1.get_price("яблоки")
if price is not None:
    print(f"Цена яблок: {price}")
else:
    print("Яблоки не найдены.")

store1.show_items()