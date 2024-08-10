class Blender:

    TRANS_MAP = {
        "Red Tree Frog": "mush",
        "apples": "apple juice",
        "iphone": "toxic waste",
    }

    def __init__(self):
        self.thing = None
        self.result = None

    @classmethod
    def select_result_for(cls, thing):
        return cls.TRANS_MAP.get(thing, "DIRT")

    def add(self, thing):
        self.thing = thing

    def switch_on(self):
        self.result = self.select_result_for(self.thing)
