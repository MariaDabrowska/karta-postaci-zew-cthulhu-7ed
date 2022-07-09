class IteratorCech:
    def __init__(self, cechy):
        self._cechy = cechy
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._cechy):
            cecha = self._cechy[self._index]
            self._index += 1
            return cecha
        raise StopIteration
