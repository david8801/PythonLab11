from models import *
from models import typeOfGoods
from models import resist
from models import quality
from models import builderGoods
from models.builderGoods import BuilderGoods
from models.woodenGoods import WoodenGoods
from models.lighting import Lightning
from models.plumbing import Plumbing


class builderGoodsManager:
    def __init__(self, goods_list):
        self.goods_list = goods_list

    def sort_goods_by_price(self, reverse):
        return sorted(self.goods_list, key=lambda builderGoods: builderGoods.price, reverse=reverse)

    def sort_goods_by_width(self, reverse):
        return sorted(self.goods_list, key=lambda builderGoods: builderGoods.width, reverse=reverse)

    def find_goods_by_type(self, typeOfGoods):
        return list(filter(lambda builderGoods: builderGoods.typeOfGoods == typeOfGoods, self.goods_list))


chair = WoodenGoods("Chair", 2, "wood", 100, typeOfGoods.TypeOfGoods.WOODEN_GOODS, 50, "IKEA", 50,
                    resist.Resist.WEAK_RESIST, 40)
table = WoodenGoods("Table", 5, "wood", 70, typeOfGoods.TypeOfGoods.WOODEN_GOODS, 100, "Valve", 150,
                    resist.Resist.STRONG_RESIST, 80)
latern = Lightning("Latern", 0.1, "wax", 20, typeOfGoods.TypeOfGoods.LIGHTNING, 5, "Lamborghini", 5,
                   100, quality.Quality.SHORT_TERM)
Lamp = Lightning("Lamp", 0.5, "steel", 500, typeOfGoods.TypeOfGoods.LIGHTNING, 1000, "Blizzard", 20,
                 2, quality.Quality.LONG_TERM)
washer = Plumbing("washer", 50, "ceramic", 60, typeOfGoods.TypeOfGoods.PLUMBING, 200, "Apple", 30,
                  20)
toilet = WoodenGoods("Toildet", 80, "ceramic", 40, typeOfGoods.TypeOfGoods.PLUMBING, 150, "Samsung", 40,
                     40)

goods = [chair, table, latern, Lamp, washer, toilet]
manager = builderGoodsManager(goods)
print(manager.sort_goods_by_price(False))
print("\n")
print(manager.sort_goods_by_width(True))
print("\n")
print(manager.find_goods_by_type(typeOfGoods.TypeOfGoods.PLUMBING))
