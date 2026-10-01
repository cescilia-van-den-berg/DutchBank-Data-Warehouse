import csv
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_file = project_root / "data" / "raw" / "branches.csv"

branches = [
    [1, "Tilburg Centrum", "Tilburg", "5038AB", "2015-03-01", "Open"],
    [2, "Breda Centrum", "Breda", "4811AA", "2012-06-15", "Open"],
    [3, "Eindhoven Centrum", "Eindhoven", "5611AB", "2010-09-01", "Open"],
    [4, "Rotterdam Centrum", "Rotterdam", "3011AA", "2008-01-15", "Open"],
    [5, "Amsterdam Zuid", "Amsterdam", "1077AA", "2005-04-01", "Closed"]
]

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "branch_id",
        "branch_name",
        "city",
        "postcode",
        "opening_date",
        "branch_status"
    ])

    writer.writerows(branches)