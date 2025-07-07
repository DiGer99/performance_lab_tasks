from pathlib import Path

import typer

app = typer.Typer()

def count_steps(nums: list[int]) -> int:
    nums.sort()

    median = nums[len(nums) // 2]
    total = sum(abs(num - median) for num in nums)

    return total


@app.command()
def main(
    nums_path: Path = typer.Argument(..., help="Path to nums file"),
):
    with open(nums_path) as f:
        res = [int(i.strip()) for i in f.readlines()]

    total = count_steps(res)
    typer.echo(total)


if __name__ == "__main__":
    app()