import csv
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_file = project_root / "data" / "raw" / "currencies.csv"

currencies = [
    ["EUR", "Euro"],
    ["USD", "US Dollar"],
    ["GBP", "British Pound"],
    ["CHF", "Swiss Franc"]
]

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["currency_code", "currency_name"])
    writer.writerows(currencies)