from .animal import Animal

class CyberSheep(Animal):
    color = (184, 3, 255)
    symbol = 'CS'

    def __init__(self, world, position):
        super().__init__(world, position, 11, 4)

    def __str__(self):
        return 'Cyber Sheep'

    def action(self):
        pos = self.world.getClosestHogweed(self.position)
        if pos == (-1, -1):
            super().action()
            return

        d1x = self.position[0] - pos[0]
        d2x = pos[0] + (self.world.getWidth() - self.position[0])
        d1y = self.position[1] - pos[1]
        d2y = pos[1] + (self.world.getHeight() - self.position[1])
        dx = abs(d1x if abs(d1x) < abs(d2x) else d2x)
        dy = abs(d1y if abs(d1y) < abs(d2y) else d2y)
        if dx > dy:
            if abs(d1x) < abs(d2x):
                self.move(-1, 0)
            else:
                self.move(1, 0)
        else:
            if abs(d1y) < abs(d2y):
                self.move(0, -1)
            else:
                self.move(0, 1)

    def getColor(self):
        return CyberSheep.color

    def getSymbol(self):
        return CyberSheep.symbol
