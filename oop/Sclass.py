class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), 'Value must be a float!'
        self.value = round(val, 2)

    def __str__(self):
        return str(self.value)


rfm = RoundFloatManual(42.0)
print(rfm)