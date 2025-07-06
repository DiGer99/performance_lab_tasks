from task2.utils_task2 import point_in_circle


def test_point_in_circle():
    results = [0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1]
    x, y = 1, 1
    radius = 5
    points = [
        (1, 6),
        (6, 1),
        (-4, 1),
        (1, -4),
        (6, 6),
        (7, 1),
        (-5, -5),
        (10, 10),
        (1, 1),
        (2, 2),
        (-3, 0),
        (-3, 2),
    ]
    for i, j in zip(point_in_circle(x, y, radius, points), results):
        assert i == j
