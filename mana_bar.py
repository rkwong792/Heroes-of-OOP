class ManaBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {
        "blue": "\33[34m",
        "default": "\033[0m"
    }

    def __init__(self, entity, length: int = 20, is_colored: bool = True) -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.mana
        self.current_value = entity.mana

        self.is_colored = is_colored
        self.color = self.colors["blue"] if is_colored else self.colors["default"]

    def update(self) -> None:
        self.current_value = self.entity.mana

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s MANA: {self.entity.mana}/{self.entity.mana_max}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")
