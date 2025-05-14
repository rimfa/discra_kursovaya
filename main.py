class ConvexHull:
    def __init__(self, points):
        self.points = points

    def find_starting_point(self):
        return min(self.points, key=lambda p: (p[1], p[0]))

    def polar_angle(self, p0, p1):
        import math
        return math.atan2(p1[1] - p0[1], p1[0] - p0[0])

    def distance(self, p0, p1):
        return (p1[0] - p0[0])**2 + (p1[1] - p0[1])**2

    def cross_product(self, o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def build_hull(self):
        if len(self.points) <= 1:
            return self.points

        start = self.find_starting_point()
        sorted_points = sorted(
            self.points,
            key=lambda p: (self.polar_angle(start, p), self.distance(start, p))
        )

        hull = [start]
        for pt in sorted_points:
            while len(hull) >= 2 and self.cross_product(hull[-2], hull[-1], pt) <= 0:
                hull.pop()
            hull.append(pt)

        return hull

# Пример использования
if __name__ == "__main__":
    points = [(1, 1), (2, 5), (3, 3), (5, 3), (3, 2), (2, 2), (4, 4)]
    algo = ConvexHull(points)
    hull = algo.build_hull()
    print("Выпуклая оболочка:", hull)