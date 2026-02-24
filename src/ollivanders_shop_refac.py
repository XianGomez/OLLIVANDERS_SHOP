class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# --- Clases de Lógica (Estrategias) ---

class InterfazItem:
    def __init__(self, item):
        self.item = item

    def update(self):
        # Lógica por defecto (Normal Item)
        self.item.sell_in -= 1
        degrado = 1 if self.item.sell_in >= 0 else 2
        self.item.quality = max(0, self.item.quality - degrado)

class AgedBrieLogic(InterfazItem):
    def update(self):
        self.item.sell_in -= 1
        aumento = 1 if self.item.sell_in >= 0 else 2
        self.item.quality = min(50, self.item.quality + aumento)

class BackstageLogic(InterfazItem):
    def update(self):
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 5:
            self.item.quality = min(50, self.item.quality + 3)
        elif self.item.sell_in < 10:
            self.item.quality = min(50, self.item.quality + 2)
        else:
            self.item.quality = min(50, self.item.quality + 1)

class SulfurasLogic(InterfazItem):
    def update(self):
        pass # Legendario: inmune al tiempo

class ConjuredLogic(InterfazItem):
    def update(self):
        self.item.sell_in -= 1
        degrado = 2 if self.item.sell_in >= 0 else 4
        self.item.quality = max(0, self.item.quality - degrado)

# --- Orquestador GildedRose ---

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def _get_logic(self, item):
        mapeo = {
            "Aged Brie": AgedBrieLogic,
            "Sulfuras, Hand of Ragnaros": SulfurasLogic,
            "Backstage passes to a TAFKAL80ETC concert": BackstageLogic,
            "Conjured Mana Cake": ConjuredLogic
        }
        clase_logica = mapeo.get(item.name, InterfazItem)
        return clase_logica(item)

    def update_quality(self):
        for item in self.items:
            # Obtenemos la lógica y la aplicamos directamente al objeto original
            logic = self._get_logic(item)
            logic.update()