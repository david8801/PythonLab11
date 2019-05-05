from models import typeOfGoods


class BuilderGoods:

    def __init__(self, name="noName", weight=0, material="noMaterial", height=0,
                 typeOfGoods=typeOfGoods.TypeOfGoods.WOODEN_GOODS, price=0, producer="noProducer", width=0):
        self.name = name
        self.weight = weight
        self.material = material
        self.height = height
        self.typeOfGoods = typeOfGoods
        self.price = price
        self.producer = producer
        self.width = width

    def __str__(self):
        return ('The item is called {0}, it weights {1} kg, it\'s made of {2},'
                + 'height = {3} sm, type of goods = {4}, price = '
                + ' {5}$, it\'s produced by {6}, width = {7} sm \n').format(self.name,
                                                                            self.weight,
                                                                            self.material,
                                                                            self.height,
                                                                            self.typeOfGoods,
                                                                            self.price,
                                                                            self.producer,
                                                                            self.width, )

    def __repr__(self):
        return self.__str__()
