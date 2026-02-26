class Item:
    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
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
    def updateQuality(self):
        pass

class Backstage(NormalItem):
    def update(self):
        self.item.sellIn -= 1
        if self.item.sellIn < 0:
            self.item.quality = 0
        elif self.item.sellIn < 5:
            self.item.quality = min(50, self.item.quality + 3)
        elif self.item.sellIn < 10:
            self.item.quality = min(50, self.item.quality + 2)
        else:
            self.item.quality = min(50, self.item.quality + 1)

class OllivandersShop(object):
    def __init__(self, items):
        self.items = items

    def _get_logic(self, item):
        mapeo = {
            "Aged Brie": AgedBrie,
            "Sulfuras, Hand of Ragnaros": Sulfuras,
            "Backstage passes to a TAFKAL80ETC concert": Backstage,
        }

        clase_logica = mapeo.get(item.name, NormalItem)
        return clase_logica(item)

    def updateQuality(self):
        for item in self.items:
            logic = self._get_logic(item)
            logic.updateQuality()