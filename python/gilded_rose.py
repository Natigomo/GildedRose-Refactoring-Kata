# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def disminuir_calidad(self, item):
        """Disminuye en una unidad la calidad del producto."""
        item.quality = item.quality - 1

    def aumentar_calidad(self, item):
        """Aumenta en una unidad la calidad del producto."""
        item.quality = item.quality + 1

    def update_quality(self):
        for item in self.items:
            if item.name not in ("Aged Brie", "Backstage passes to a TAFKAL80ETC concert",):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        self.disminuir_calidad(item)
            else:
                if item.quality < 50:
                    self.aumentar_calidad(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                self.aumentar_calidad(item)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                self.aumentar_calidad(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                self.disminuir_calidad(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        self.aumentar_calidad(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
