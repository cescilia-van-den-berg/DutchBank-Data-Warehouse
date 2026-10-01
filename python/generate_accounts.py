import csv
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_file = project_root / "data" / "raw" / "accounts.csv"

accounts = [
    ["ACC00001", 1, 1, "Checking", "2018-06-15", "", "Active"],
    ["ACC00002", 1, 1, "Savings", "2019-01-10", "", "Active"],
    ["ACC00003", 2, 2, "Checking", "2019-02-20", "", "Active"],
    ["ACC00004", 2, 2, "Savings", "2020-03-15", "", "Active"],
    ["ACC00005", 3, 3, "Checking", "2020-09-10", "", "Active"],
    ["ACC00006", 4, 4, "Checking", "2015-03-05", "", "Active"],
    ["ACC00007", 4, 4, "Savings", "2016-07-20", "", "Active"],
    ["ACC00008", 5, 5, "Checking", "2017-11-22", "2024-05-31", "Closed"],
    ["ACC00009", 6, 1, "Checking", "2021-01-18", "", "Active"],
    ["ACC00010", 6, 1, "Savings", "2021-06-01", "", "Active"],
    ["ACC00011", 7, 2, "Checking", "2016-05-30", "2023-12-31", "Closed"],
    ["ACC00012", 8, 3, "Checking", "2018-09-17", "", "Active"],
    ["ACC00013", 9, 4, "Checking", "2022-04-11", "", "Active"],
    ["ACC00014", 10, 5, "Savings", "2014-08-25", "2022-10-15", "Closed"],
    ["ACC00015", 10, 5, "Checking", "2015-02-01", "", "Active"]
]

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "account_id",
        "customer_id",
        "branch_id",
        "account_type",
        "open_date",
        "close_date",
        "account_status"
    ])

    writer.writerows(accounts)