from tabulate import tabulate


def write_data(data: list[dict[str, str]]) -> None:
    print(tabulate(
        data,
        headers="keys",
        tablefmt="grid"   
    ))
