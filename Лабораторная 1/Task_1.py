import doctest
class Clothing:
    """
    Класс для описания одежды.
    Атрибуты:
        size (str): Размер одежды.
        color (str): Цвет одежды.
    """
    def __init__(self, size: str, color: str):
        if size not in ("XS", "S", "M", "L", "XL", "XXL"):
            raise ValueError("Недопустимый размер одежды. Выберите из: XS, S, M, L, XL, XXL.")
        if not isinstance(color, str) or not color:
            raise ValueError("Цвет должен быть непустой строкой.")
        self.size = size
        self.color = color
    def wash(self) -> str:
        """
        Постирать одежду.
        :return: Сообщение об успешной стирке.
        Примеры:
        >>> shirt = Clothing("M", "синий")
        >>> shirt.wash()
        'Одежда размером M и цвета синий постирана.'
        """
        return f"Одежда размером {self.size} и цвета {self.color} постирана."
    def iron(self) -> str:
        """
        Погладить одежду.
        :return: Сообщение об успешной глажке.
        Примеры:
        >>> pants = Clothing("L", "черный")
        >>> pants.iron()
        'Одежда размером L и цвета черный поглажена.'
        """
        return f"Одежда размером {self.size} и цвета {self.color} поглажена."
class Footwear:
    """
    Класс для описания обуви.
    Атрибуты:
        size (float): Размер обуви (поддерживает половинки, например, 36.5).
        material (str): Материал, из которого изготовлена обувь.
    """
    def __init__(self, size: float, material: str):
        if not isinstance(size, (int, float)) or size < 36 or size > 46:
            raise ValueError("Размер обуви должен быть числом от 36 до 46, включая половинки.")
        if not isinstance(material, str) or not material:
            raise ValueError("Материал должен быть непустой строкой.")
        self.size = size
        self.material = material
    def polish(self) -> str:
        """
        Начистить обувь.
        :return: Сообщение об успешной чистке.
        Примеры:
        >>> shoes = Footwear(42, "кожа")
        >>> shoes.polish()
        'Обувь размера 42 из материала кожа начищена.'
        """
        return f"Обувь размера {self.size} из материала {self.material} начищена."
    def replace_sole(self) -> str:
        """
        Заменить подошву.
        :return: Сообщение об успешной замене подошвы.
        Примеры:
        >>> boots = Footwear(45, "замша")
        >>> boots.replace_sole()
        'Подошва на обуви размера 45 из материала замша заменена.'
        """
        return f"Подошва на обуви размера {self.size} из материала {self.material} заменена."
class Accessory:
    """
    Класс для описания аксессуаров.
    Атрибуты:
        type (str): Тип аксессуара (например, "часы", "сумка", "шарф").
        brand (str): Бренд аксессуара.
    """
    def __init__(self, type: str, brand: str):
        if not isinstance(type, str) or not type:
            raise ValueError("Тип аксессуара должен быть непустой строкой.")
        if not isinstance(brand, str) or not brand:
            raise ValueError("Бренд должен быть непустой строкой.")
        self.type = type
        self.brand = brand
    def clean(self) -> str:
        """
        Почистить аксессуар.
        :return: Сообщение об успешной чистке.
        Примеры:
        >>> bag = Accessory("сумка", "Gucci")
        >>> bag.clean()
        'Аксессуар типа сумка от бренда Gucci почищен.'
        """
        return f"Аксессуар типа {self.type} от бренда {self.brand} почищен."
    def pack(self) -> str:
        """
        Упаковать аксессуар.
        :return: Сообщение об успешной упаковке.
        Примеры:
        >>> scarf = Accessory("шарф", "Hermes")
        >>> scarf.pack()
        'Аксессуар типа шарф от бренда Hermes упакован.'
        """
        return f"Аксессуар типа {self.type} от бренда {self.brand} упакован."
if __name__ == "__main__":
    doctest.testmod()  # Проверка примеров из документации
    pass
