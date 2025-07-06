from task2.utils_task2 import point_in_circle
from pathlib import Path
import typer

app = typer.Typer()


@app.command()
def main(
    file_1: Path = typer.Argument(..., help="Файл с описанием круга"),
    file_2: Path = typer.Argument(..., help="Файл с точками"),
):
    with open(file_1) as f:
        res = f.readlines()
        x, y = map(int, res[0].split())
        radius = int(res[1])

    with open(file_2) as fl:
        res = fl.readlines()
        res = [tuple(i.split()) for i in res]
        points = [tuple(map(int, i)) for i in res]

    result = point_in_circle(x, y, radius, points)

    typer.echo(result)


if __name__ == "__main__":
    app()
