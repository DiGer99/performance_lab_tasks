import json
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def main(
    values_file: Path = typer.Argument(),
    tests_file: Path = typer.Argument(),
    report_file: Path = typer.Argument(),
):
    with open(values_file) as f:
        values_data = json.load(f)

    values = {item["id"]: item["value"] for item in values_data["values"]}

    def find_values(tests):
        for test in tests:
            test_id = test.get("id")
            if test_id in values:
                test["value"] = values[test_id]
            if "values" in test:
                find_values(test["values"])

    with open(tests_file) as f:
        tests_data = json.load(f)

    find_values(tests_data["tests"])

    with open(report_file, "w") as f:
        json.dump(tests_data, f, indent=2)


if __name__ == "__main__":
    app()
