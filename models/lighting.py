from models import typeOfGoods
from models import builderGoods
from models import  quality
from models.builderGoods import BuilderGoods

class Lightning(BuilderGoods):
    def __init__(self, name="noName", weight=0, material="noMaterial", height=0, typeOfGoods=typeOfGoods.TypeOfGoods.WOODEN_GOODS, price=0, producer="noProducer", width=0, quantity=0, quality=quality.Quality.LONG_TERM):
        super(Lightning, self).__init__(name, weight, material, height, typeOfGoods, price, producer, width)
        self.quantity = quantity
        self.quality = quality

    def __str__(self):
        return ('The item is called {0}, it weights {1} kg, it\'s made of {2},'
                + 'height = {3} sm, type of goods = {4}, price = '
                + ' {5}$, it\'s produced by {6}, width = {7} sm, quantity = {8}, quality = {9} \n').format(self.name,
                                                           self.weight, self.material, self.height,
                                                           self.typeOfGoods,
                                                           self.price,
                                                           self.producer, self.width, self.quantity, self.quality)

    def __repr__(self):
        return self.__str__()
