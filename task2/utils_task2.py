def point_in_circle(x: int, y: int, radius: int, points: list[tuple[int, int]]):
    res = []

    for idx, el in enumerate(points):
        x_point, y_point = el
        if (x_point - x) ** 2 + (y_point - y) ** 2 < radius**2:
            res.append(1)

        elif (x_point - x) ** 2 + (y_point - y) ** 2 > radius**2:
            res.append(2)

        elif (x_point - x) ** 2 + (y_point - y) ** 2 == radius**2:
            res.append(0)

    return res
