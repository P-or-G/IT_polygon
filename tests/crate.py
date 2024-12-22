import unittest
from random import uniform, randint
from crate import *

class TestCrates(unittest.TestCase):
    def test_ok(self):
        uid = 1
        h, w, l = uniform(1, 100), uniform(1, 100), uniform(1, 100)

        c = Crate(uid, l,  w,  h)
        self.assertEqual(c.length(), l)
        self.assertEqual(c.width(), w)
        self.assertEqual(c.height(), h)
        self.assertAlmostEqual(c.volume(), h * w * l)


        uid = 100
        h, w, l = randint(1, 100), randint(1, 100), randint(1, 100)

        c = Crate(uid, l,  w,  h)
        self.assertEqual(c.length(), l)
        self.assertEqual(c.width(), w)
        self.assertEqual(c.height(), h)
        self.assertAlmostEqual(c.volume(), h * w * l)

    def test_negative(self):
        uid = 1
        h, w, l = -uniform(1, 100), uniform(1, 100), uniform(1, 100)
        with self.assertRaises(NonpositiveSide):
            Crate(uid, uid, h,  w,  l)

        h, w, l = uniform(1, 100), -uniform(1, 100), uniform(1, 100)
        with self.assertRaises(NonpositiveSide):
            Crate(uid, h,  w,  l)

        h, w, l = uniform(1, 100), uniform(1, 100), -uniform(1, 100)
        with self.assertRaises(NonpositiveSide):
            Crate(uid, h,  w,  l)


    def test_zero(self):
        uid = 1
        h, w, l = 0, uniform(1, 100), -uniform(1, 100)
        with self.assertRaises(NonpositiveSide):
            Crate(uid, h,  w,  l)

        h, w, l = uniform(1, 100), 0, -uniform(1, 100)
        with self.assertRaises(NonpositiveSide):
            Crate(uid, h,  w,  l)

        h, w, l = uniform(1, 100), uniform(1, 100), 0
        with self.assertRaises(NonpositiveSide):
            Crate(uid, h,  w,  l)


    def test_invalid_id(self):
        h, w, l = 1, 1, 1
        uid = 0.1

        with self.assertRaises(InvalidId):
            Crate(uid, h, w, l)

        uid = "abcd"
        with self.assertRaises(InvalidId):
            Crate(uid, h, w, l)

    def test_invalid_side(self):
        uid = 1

        h, w, l = "abcd", uniform(1, 100), uniform(1, 100)
        with self.assertRaises(InvalidSide):
            Crate(uid, h,  w,  l)

        h, w, l = "abcd", uniform(1, 100), "lol"
        with self.assertRaises(InvalidSide):
            Crate(uid, h,  w,  l)

        h, w, l = uniform(1,100), "abbbb", uniform(1, 100)
        with self.assertRaises(InvalidSide):
            Crate(uid, h,  w,  l)


class TestCrateCollections(unittest.TestCase):
    def test_ok(self):
        crates = [Crate(1, 1, 1, 1), Crate(2, 2, 2, 2), Crate(3, 3, 3, 3)]
        cc = CrateCollection.fromCrates(crates)

        self.assertEqual(crates, cc.getCrates())

    def test_duplicates(self):
        crates = [Crate(1, 1, 1, 1), Crate(1, 2, 2, 2), Crate(3, 3, 3, 3)]

        with self.assertRaises(DuplicateCrate):
            CrateCollection.fromCrates(crates)

    def test_vol_sort(self):
        n = 10
        crates = [Crate(i, i + 1, i + 2, i + 3, i + 4) for i in range(n)]
        cc = CrateCollection.fromCrates(crates)

        srtd = sorted(crates, key=lambda c: c.length() * c.width() * c.height())

        self.assertEqual(cc.sortByVolume(), srtd)

if __name__ == "__main__":
    unittest.main()
