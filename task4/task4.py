from pathlib import Path

import typer

from task4.task4_utils import count_steps

app = typer.Typer()


@app.command()
def main(
    nums_path: Path = typer.Argument(
        ...,
        help="Path to nums file",
    ),
):
    with open(nums_path) as f:
        res = [int(i.strip()) for i in f.readlines()]

    total = count_steps(res)
    typer.echo(total)


if __name__ == "__main__":
    app()
