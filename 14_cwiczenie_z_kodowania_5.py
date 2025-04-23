'''
Ćwiczenie 5
Załóżmy, że pracujesz nad klasą o nazwie Point, która reprezentuje punkt w dwuwymiarowej przestrzeni i ma następujące atrybuty:

x: współrzędna x punktu
y: współrzędna y punktu

Potrzebujesz zaimplementować metodę __eq__() tej klasy, która porównuje dwa obiekty klasy Point na podstawie ich współrzędnych.

Przykłady:
[IN]: point1 = Point(1, 2)
[IN]: point2 = Point(1, 2)
[IN]: point3 = Point(4, 3)
 
[IN]: point1 == point2
[OUT]: True
[IN]: point1 == point3
[OUT]: False
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


point1 = Point(2, 3)
point2 = Point(2, 3)
point3 = Point(4, 5)

print(point1 == point2)
print(point1 == point3)
