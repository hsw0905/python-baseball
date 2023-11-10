class NumberDto:
    def __init__(self, numbers: list[int]):
        self._numbers = numbers

    @property
    def numbers(self):
        return self._numbers
