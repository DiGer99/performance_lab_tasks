import typer
from task1.utils_task1 import way_array


app = typer.Typer()


@app.command()
def main(
    n: int = typer.Argument(..., help="Длина массива"),
    m: int = typer.Argument(..., help="Шаг обхода"),
):
    res = way_array(n, m)
    typer.echo(res)


if __name__ == "__main__":
    app()
