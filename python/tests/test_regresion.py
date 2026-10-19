import pytest

from gilded_rose import GildedRose, Item


@pytest.mark.parametrize(
    "nombre,venta,calidad,venta_esperada,calidad_esperada",
    [
        ("Producto normal", 5, 10, 4, 9),
        ("Producto normal", 0, 10, -1, 8),
        ("Aged Brie", 5, 10, 4, 11),
        ("Aged Brie", 0, 10, -1, 12),
        ("Backstage passes to a TAFKAL80ETC concert", 15, 10, 14, 11),
        ("Backstage passes to a TAFKAL80ETC concert", 10, 10, 9, 12),
        ("Backstage passes to a TAFKAL80ETC concert", 5, 10, 4, 13),
        ("Backstage passes to a TAFKAL80ETC concert", 0, 10, -1, 0),
        ("Sulfuras, Hand of Ragnaros", 5, 80, 5, 80),
        ("Producto normal", 5, 0, 4, 0),
        ("Aged Brie", 5, 50, 4, 50),
        ("Backstage passes to a TAFKAL80ETC concert", 5, 50, 4, 50),
    ],
)
def test_actualizacion_productos(
    nombre, venta, calidad, venta_esperada, calidad_esperada
):
    producto = Item(nombre, venta, calidad)
    sistema = GildedRose([producto])

    sistema.update_quality()

    assert producto.sell_in == venta_esperada
    assert producto.quality == calidad_esperada