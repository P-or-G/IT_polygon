class Crate:
    def __init__(self, uid, length, width, height, arg1 = None, arg2 = None, arg3 = None):
        if not isinstance(length, float | int):
           raise InvalidSide(length)
        if not isinstance(width, float | int):
           raise InvalidSide(width)
        if not isinstance(height, float | int):
           raise InvalidSide(height)

        if not isinstance(uid, int):
           raise InvalidId(uid)

        if length <= 0:
            raise NonpositiveSide(length)
        if width <= 0:
            raise NonpositiveSide(width)
        if height <= 0:
            raise NonpositiveSide(height)

        self._uid = uid
        self._length = length
        self._width = width
        self._height = height

        self._volume = length * width * height

    def setLength(self, length):
        if length <= 0:
            raise NonpositiveSide(length)
        else:
            self._volume = length * self._width * self._height
            self._length = length

    def setWidth(self, width):
        if width <= 0:
            raise NonpositiveSide(width)
        else:
            self._volume = self._length * width * self._height
            self._width = width

    def setHeight(self, height):
        if height <= 0:
            raise NonpositiveSide(height)
        else:
            self._volume = self._length * self._width * height
            self._height = height

    def setSizes(self, *, l = None, w = None, h = None):
        if not l:
            l = self._length
        if not w:
            w = self._width
        if not h:
            h = self._height

        self.setLength(l)
        self.setWidth(w)
        self.setHeight(h)
        self._volume = l * w * h

    def length(self):
        return self._length
    def width(self):
        return self._width
    def height(self):
        return self._height
    def volume(self):
        return self._volume
    def uid(self):
        return self._uid

    def __repr__(self) -> str:
        return f"Ящик №{self.uid()} объёмом {self.volume()}"

class CrateCollection:
    def __init__(self, crates = {}):
        self.crates = crates

    @classmethod
    def fromCrates(cls, crates):
        crates_dict = {}
        for c in crates:
            if c.uid() in crates_dict:
                raise DuplicateCrate(c.uid())

            crates_dict[c.uid()] = c

        return cls(crates_dict)

    def addCrate(self, c):
        self.crates[c.uid()] = c

    def findById(self, uid):
        return self.crates[uid]

    def sortByVolume(self, rev = False):
        return sorted(self.crates.values(), key=lambda c: c.volume(), reverse=rev)

    def getCrates(self):
        return list(self.crates.values())


class InvalidSide(Exception):
    msg = "Попытка создать ящик с неправильной стороной"

    def __init__(self, val) -> None:
        super().__init__(f"{self.msg}: ${val}")

class NonpositiveSide(Exception):
    msg = "Попытка создать ящик с неположительной стороной"

    def __init__(self, val) -> None:
        super().__init__(f"{self.msg}: {val}")

class NonpostiveVolume(Exception):
    msg = "Попытка создать ящик с неположительным объёмом"

    def __init__(self, val) -> None:
        super().__init__(f"{self.msg}: {val}")

class InvalidId(Exception):
    msg = "Попытка создать ящик с неправильным идентификатором"

    def __init__(self, val) -> None:
        super().__init__(f"{self.msg}: {val}")

class DuplicateCrate(Exception):
    msg = "Попытка создать ящик с уже существующим идентификатором"

    def __init__(self, val) -> None:
        super().__init__(f"{self.msg}: {val}")

