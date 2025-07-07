from task4.task4_utils import count_steps
from pytest import mark


@mark.parametrize(
    "nums, result",
    [
        ([100], 0),
        ([3, 1], 2),
        ([5, 5, 5, 5], 0),
        ([1, 10, 2, 9], 16),
        ([100, 2, 1], 99),
        ([1, 2, 3, 4, 5], 6),
    ],
)
def test_count_steps(
    nums,
    result,
):
    assert count_steps(nums) == result
