from task1.utils_task1 import way_array


def test_way_array():
    tests_ex = [
        (4, 3, "13"),
        (5, 4, "14253"),
        (6, 4, "14"),
        (3, 3, "132"),
        (7, 2, "1234567"),
    ]
    for i in tests_ex:
        assert way_array(i[0], i[1]) == i[2]
