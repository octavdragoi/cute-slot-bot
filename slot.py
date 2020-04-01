import numpy as np

items = ["<3", ":*", ">:D<"]

class CuteSlotMachine:
    def __init__(self, size = 5, items = items):
        self.size = size
        self.items = items
        self.n_items = len(items)

    def spin(self):
        draw_idx = np.random.randint(self.n_items, size = self.size)
        draw = [items[x] for x in draw_idx]
        return draw


if __name__ == "__main__":
    # do tests
    csm = CuteSlotMachine()
    print (csm.spin())



