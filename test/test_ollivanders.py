from __future__ import print_function

from src.ollivanders_shop import *


def main():
    print("OMGHAI!")
    items = [
        Item(name="+5 Dexterity Vest", sellIn=10, quality=20),
        Item(name="Aged Brie", sellIn=2, quality=0),
        Item(name="Elixir of the Mongoose", sellIn=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sellIn=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sellIn=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sellIn=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sellIn=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sellIn=5, quality=49),
        Item(name="Conjured Mana Cake", sellIn=3, quality=6),  # <-- :O
    ]
    days = 15
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        OllivandersShop(items).updateQuality()


if __name__ == "__main__":
    main()