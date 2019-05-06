from math import sqrt


class Node:
    def __init__(self, city, x, y):
        self.city = city
        self.x = x
        self.y = y

    def __str__(self):
        return '{}, {}, {}'.format(self.city, self.x , self.y)

    def get_distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
