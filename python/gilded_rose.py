# Define the basic Item class with name, sell_in (days left to sell), and quality
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name              # Item name (used to identify behavior rules)
        self.sell_in = sell_in        # Days remaining to sell the item
        self.quality = quality        # Item quality (0 <= quality <= 50 normally)

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


# The GildedRose class is responsible for updating the items every day
class GildedRose:
    def __init__(self, items):
        self.items = items  # List of Item objects managed by the system

    def update_quality(self):
        # Loop through all items and update them individually
        for item in self.items:
            self._update_item(item)

    def _update_item(self, item):
        # Sulfuras is a legendary item and does not change at all
        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        # Delegate update logic based on item name
        if item.name == "Aged Brie":
            self._update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self._update_backstage_pass(item)
        elif item.name.startswith("Conjured"):
            self._update_conjured_item(item)
        else:
            self._update_regular_item(item)

        # All items except Sulfuras lose 1 day from sell_in
        item.sell_in -= 1

    def _increase_quality(self, item, amount=1):
        # Quality cannot exceed 50 (except for Sulfuras, which we skip here)
        item.quality = min(item.quality + amount, 50)

    def _decrease_quality(self, item, amount=1):
        # Quality cannot go below 0
        item.quality = max(item.quality - amount, 0)

    def _update_aged_brie(self, item):
        # Aged Brie increases in quality the older it gets
        self._increase_quality(item)
        # If it's past the sell_in date, it gains quality even faster
        if item.sell_in <= 0:
            self._increase_quality(item)

    def _update_backstage_pass(self, item):
        # Backstage passes increase in quality as the concert approaches
        if item.sell_in > 10:
            self._increase_quality(item)         # More than 10 days left
        elif item.sell_in > 5:
            self._increase_quality(item, 2)      # 6-10 days left
        elif item.sell_in > 0:
            self._increase_quality(item, 3)      # 1-5 days left
        else:
            item.quality = 0                     # After the concert, quality drops to 0

    def _update_conjured_item(self, item):
        # Conjured items degrade in quality twice as fast
        self._decrease_quality(item, 2)
        # After sell_in date, they degrade even faster
        if item.sell_in <= 0:
            self._decrease_quality(item, 2)

    def _update_regular_item(self, item):
        # Normal items lose quality every day
        self._decrease_quality(item)
        # After sell_in, they lose quality twice as fast
        if item.sell_in <= 0:
            self._decrease_quality(item)


# Optional example usage: this lets you simulate the behavior over several days
if __name__ == "__main__":
    items = [
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    ]

    gr = GildedRose(items)

    for day in range(1, 6):  # Simulate 5 days
        print(f"\n--- Day {day} ---")
        for item in items:
            print(item)
        gr.update_quality()
