# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        # Create a single item named "foo" with sell_in = 0 and quality = 0
        items = [Item("foo", 0, 0)]

        # Pass the item into the GildedRose system
        gilded_rose = GildedRose(items)

        # Update quality (this will apply business rules — in this case, none are specific to "foo")
        gilded_rose.update_quality()

        # Check that the item's name hasn't changed
        self.assertEqual("foo", items[0].name)


if __name__ == '__main__':
    unittest.main()
