"""Add from_k(cls, k) to build from Kelvin (K→C = K − 273.15)."""


class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    # instance method: needs 'self'
    def to_f(self) -> float:
        return self.celsius * 9 / 5 + 32

    # class method: first arg is 'cls'
    @classmethod
    def from_f(cls, f: float):
        return cls((f - 32) * 5 / 9)

    # static method: utility; no self/cls
    @staticmethod
    def is_valid(temp: float) -> bool:
        return -273.15 <= temp <= 1e6

    # Added from_k -> from K to celcius
    @classmethod
    def from_k(cls, k: float):
        return cls((k - 273.15))


# Writing the main function
if __name__ == "__main__":

    t = Temperature.from_k(284.82)
    print(t.is_valid(t.celsius))

    print(f"Temperature in Celsius: {t.celsius}")

    """
    This means you must call it like this:

Temperature.is_valid(temp_value)


or

t.is_valid(temp_value)


(both work, since it’s static).
    """
