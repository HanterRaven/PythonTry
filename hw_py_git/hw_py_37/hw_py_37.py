from shapes import circle
from shapes import rectangle
from shapes import cylinder

circles = [circle.Circle(4), circle.Circle(2), circle.Circle(6), circle.Circle(8), circle.Circle(1)]
rects = [rectangle.Rectangle(3, 7), rectangle.Rectangle(2, 7), rectangle.Rectangle(19, 12)]
cylinders = [cylinder.Cylinder(4, 7), cylinder.Cylinder(2, 5), cylinder.Cylinder(9, 3), cylinder.Cylinder(5, 5)]
circle_max_s = max(circles, key=lambda c: c.get_circle_square())
rect_min_p = min(rects, key=lambda r: r.get_rect_perimeter())
cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
cylinders_v_avg = sum(cylinders_v) / len(cylinders_v)
print('*' * 50)
print('Окружность с наибольшей площадью:', end=' ')
circle_max_s.print_circle()
print('Прямоугольник с наименьшим периметром:', end=' ')
rect_min_p.print_rect()
print(f'Средний объем всех цилиндров: {cylinders_v_avg:.2f}')
