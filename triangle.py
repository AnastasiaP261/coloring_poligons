triangles = []


class Point:
    def __init__(self, _id, x, y):
        self.id = _id
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, _id, p1, p2, p3):
        self.id = _id - 1
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.connections = dict()
        self.allow_colors = [0, 1, 2, 3]

        for trian in triangles:
            if trian.id != self.id and self.check_connect(trian):
                if trian.id not in self.connections:
                    self.connections[trian.id] = trian
                    trian.connections[self.id] = self

    def check_connect(self, trian):
        count = 0
        for p in (self.p1, self.p2, self.p3):
            for pt in (trian.p1, trian.p2, trian.p3):
                if p.id == pt.id:
                    count += 1
        if count >= 2:
            return True

    def coloring(self):
        if len(self.connections) == 0:
            self.allow_colors = self.allow_colors[0]
        for trian in self.connections.values():
            if type(trian.allow_colors) == list:
                trian.except_colors()
                trian.allow_colors = trian.allow_colors[0]


    def except_colors(self):
        for trian in self.connections.values():
            if type(trian.allow_colors) == int:
                try:
                    self.allow_colors.remove(trian.allow_colors)
                except ValueError:
                    pass


