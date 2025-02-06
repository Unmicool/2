class Flower:
    """Базовый класс для цветов"""
    def __init__(self, name: str, color: str):
        self._name = name  # Название цветка
        self._color = color  # Цвет лепестков

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> str:
        return self._color

    def bloom(self) -> str:
        """Метод, отображающий процесс цветения"""
        return f"{self.name} расцветает красивыми {self.color} лепестками."

    def __str__(self) -> str:
        return f"Цветок {self.name}, цвет {self.color}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, color={self.color!r})"

class Rose(Flower):
    """Дочерний класс для роз"""

    def __init__(self, name: str, color: str, thorny: bool):
        super().__init__(name, color)
        self.thorny = thorny  # Наличие шипов

    def smell(self) -> str:
        """Метод, специфичный для роз, отображает их аромат"""
        return f"{self.name} источает прекрасный аромат."

    def __str__(self) -> str:
        return f"Роза {self.name}, цвет {self.color}, {'с шипами' if self.thorny else 'без шипов'}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, color={self.color!r}, thorny={self.thorny})"

class Tulip(Flower):
    """Дочерний класс для тюльпанов"""

    def bloom(self) -> str:
        return f"{self.name} раскрывает свои {self.color} лепестки на солнце."

class Lily(Flower):
    """Дочерний класс для лилий"""

    def smell(self) -> str:
        return f"{self.name} обладает нежным ароматом."

class Sunflower(Flower):
    """Дочерний класс для подсолнухов"""
    def follow_sun(self) -> str:
        return f"{self.name} поворачивается за солнцем в течение дня."

if __name__ == "__main__":
    rose = Rose(name="Красная роза", color="красный", thorny=True)
    tulip = Tulip(name="Желтый тюльпан", color="желтый")
    lily = Lily(name="Белая лилия", color="белый")
    sunflower = Sunflower(name="Солнечный подсолнух", color="желтый")

    print(rose)
    print(repr(rose))
    print(rose.bloom())
    print(rose.smell())

    print(tulip.bloom())
    print(lily.smell())
    print(sunflower.follow_sun())
