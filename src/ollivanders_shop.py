class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sellIn = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sellIn, self.quality)

class NormalItem:
    def __init__(self, item):
        self.item = item

    def updateQuality(self):
        self.item.sellIn -= 1
        degrado = 1 if self.item.sellIn >= 0 else 2
        self.item.quality = max(0, self.item.quality - degrado)

class AgedBrie(NormalItem):
    def updateQuality(self):
        self.item.sellIn -= 1
        aumento = 1 if self.item.sellIn >= 0 else 2
        self.item.quality = min(50, self.item.quality + aumento)

class Sulfuras(NormalItem):
    def updateQQuality(self):
        pass