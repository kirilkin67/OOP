class Product:
    def __init__(self, name, weight: float, price: float, category):
        self.name = name
        self.weight = weight
        self.price = price
        self.category = category

    def __str__(self):
        return f"[{self.name}, вес: {self.weight:0.3f}кг, цена: {self.price:0.2f}руб]"

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


class Cart:
    def __init__(self, products=None):
        if products is None:
            self.products = list()
        else:
            self.products = products

    def add_product(self, product: Product, count: int):
        for p in self.products:
            if p[0] == product:
                p[1] += count
                break
        else:
            self.products.append([product, count])

    def get_weight(self):
        return sum(p[0].weight * p[1] for p in self.products)

    def get_total_price(self):
        return sum(p[0].price * p[1] for p in self.products)

    def __str__(self):
        content = "\n".join(f"- {p[0]} к-во: {p[1]}шт." for p in self.products)
        return f"Вес: {self.get_weight():0.3f}кг\nСтоимость: {self.get_total_price():0.2f}руб\nСодержимое:\n{content}"

    def __eq__(self, other):
        return self.get_weight() == other.get_weight()

    def __add__(self, other):
        return Cart(self.products + other.products)

    def __iadd__(self, other):
        self.products += other.products
        return self

    def __iter__(self):
        return iter(self.products)

    def __lt__(self, other):
        if not isinstance(other, Cart):
            return False
        return self.get_total_price() < other.get_total_price()

    def __gt__(self, other):
        if not isinstance(other, Cart):
            return False
        return self.get_total_price() > other.get_total_price()


if __name__ == "__main__":
    product_1 = Product("Яблоко", 0.2, 50, "Фрукты")
    product_2 = Product("Молоко", 1, 70, "Молочные продукты")
    product_3 = Product("Хлеб", 0.5, 30, "Хлебобулочные изделия")
    product_4 = Product("Бананы", 1, 105.99, "Фрукты")

    cart_1 = Cart()
    cart_1.add_product(product_1, 3)
    cart_1.add_product(product_1, 1)
    cart_1.add_product(product_2, 2)
    cart_1.add_product(product_3, 2)
    cart_1.add_product(product_4, 3)

    print("Корзина 1")
    print(cart_1)
    print()

    print("Корзина 2")
    cart_2 = Cart()
    cart_2.add_product(product_2, 1)
    cart_2.add_product(product_3, 4)
    print(cart_2)
    print()

    cart_3 = Cart(cart_2)
    print(cart_2 == cart_3)
    print(cart_3)
    print()

    print("Корзина 3")
    cart_3 = cart_1 + cart_2
    print(cart_2 == cart_3)
    print(cart_3)
    print()

    print("Корзина 1")
    cart_1 += cart_2
    print(cart_1)
