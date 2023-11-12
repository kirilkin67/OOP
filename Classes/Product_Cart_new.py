class Product:
    def __init__(self, name, weight, price, category):
        self.name = name
        self.weight = weight
        self.price = price
        self.category = category

    def __str__(self):
        return f"[{self.name}, вес: {self.weight}кг, цена: {self.price}р]"

    def __eq__(self, other):
        return self.price / self.weight == other.price / other.weight

    def __lt__(self, other):
        if not isinstance(other, Product):
            return False
        return self.price_per_weight() < other.price_per_weight()

    def __gt__(self, other):
        if not isinstance(other, Product):
            return False
        return self.price_per_weight() > other.price_per_weight()

    def price_per_weight(self):
        return self.price / self.weight

    def serialize(self):
        return f"{self.name},{self.weight},{self.price},{self.category}"

    @staticmethod
    def deserialize(serialized_str):
        name, weight, price, category = serialized_str.split(",")
        return Product(name, float(weight), float(price), category)


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        for p in self.products:
            if p[0] == product:
                p[1] += quantity
                break
        else:
            self.products.append([product, quantity])

    def get_weight(self):
        return sum(p[0].weight * p[1] for p in self.products)

    def get_total_price(self):
        return sum(p[0].price * p[1] for p in self.products)

    def __str__(self):
        content = "\n".join(f"- {p[0]} к-во: {p[1]}шт." for p in self.products)
        return f"Вес: {self.get_weight()}кг\nСтоимость: {self.get_total_price()}р\nСодержимое:\n{content}"

    def __eq__(self, other):
        return self.get_weight() == other.get_weight()

    def __add__(self, other):
        new_cart = Cart()
        new_cart.products = self.products + other.products
        return new_cart

    def __iadd__(self, other):
        self.products += other.products
        return self

    def __iter__(self):
        return iter(self.products)

    def serialize(self):
        serialized_products = [f"{p[0].serialize()}|{p[1]}" for p in self.products]
        return ";".join(serialized_products)

    def __lt__(self, other):
        if not isinstance(other, Cart):
            return False
        return self.get_total_price() < other.get_total_price()

    def __gt__(self, other):
        if not isinstance(other, Cart):
            return False
        return self.get_total_price() > other.get_total_price()

    @staticmethod
    def deserialize(serialized_str):
        cart = Cart()
        for serialized_product in serialized_str.split(";"):
            product_str, quantity_str = serialized_product.split("|")
            product = Product.deserialize(product_str)
            quantity = int(quantity_str)
            cart.add_product(product, quantity)
        return cart


product1 = Product("Яблоко", 0.2, 50, "Фрукты")
product2 = Product("Молоко", 1, 70, "Молочные продукты")
product3 = Product("Хлеб", 0.5, 30, "Хлебобулочные изделия")

print(product1 == product2)  # False
print(product1 == product3)  # True

print(product1 > product2)
print(product1 < product3)

cart1 = Cart()
cart1.add_product(product1, 3)
cart1.add_product(product2, 2)
print(cart1)

cart2 = Cart()
cart2.add_product(product2, 1)
cart2.add_product(product3, 4)
print(cart2)

cart3 = cart1 + cart2
print(cart3)

cart1 += cart2
print(cart1)

print(cart1 == cart2)

print(cart1 > cart2)
print(cart1 < cart2)

serialized_cart = cart1.serialize()
print(serialized_cart)
deserialized_cart = Cart.deserialize(serialized_cart)
print(deserialized_cart)

print(cart1)
print(product1)

for product, quantity in cart1:
    print(f"Товар: {product}, Кол-во: {quantity}")
