import csv
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_file = project_root / "data" / "raw" / "transactions.csv"

transactions = [
    ["TXN00001", "ACC00001", 1, "2024-01-05 09:15:00", "Purchase", 45.80, "EUR", "Completed"],
    ["TXN00002", "ACC00001", 2, "2024-01-07 14:30:00", "Purchase", 72.35, "EUR", "Completed"],
    ["TXN00003", "ACC00001", 4, "2024-01-10 08:20:00", "Purchase", 55.00, "EUR", "Completed"],
    ["TXN00004", "ACC00001", "", "2024-01-12 10:00:00", "Deposit", 500.00, "EUR", "Completed"],
    ["TXN00005", "ACC00001", "", "2024-01-15 16:45:00", "Transfer", 200.00, "EUR", "Completed"],

    ["TXN00006", "ACC00002", 10, "2024-01-06 11:25:00", "Purchase", 89.99, "EUR", "Completed"],
    ["TXN00007", "ACC00002", 9, "2024-01-14 19:10:00", "Purchase", 24.50, "EUR", "Completed"],
    ["TXN00008", "ACC00002", "", "2024-01-20 09:00:00", "Deposit", 750.00, "EUR", "Completed"],
    ["TXN00009", "ACC00002", "", "2024-01-25 13:30:00", "Withdrawal", 100.00, "EUR", "Completed"],
    ["TXN00010", "ACC00002", 11, "2024-01-28 08:45:00", "Purchase", 18.40, "EUR", "Completed"],

    ["TXN00011", "ACC00003", 3, "2024-02-02 18:20:00", "Purchase", 32.50, "EUR", "Completed"],
    ["TXN00012", "ACC00003", 1, "2024-02-05 17:15:00", "Purchase", 65.20, "EUR", "Completed"],
    ["TXN00013", "ACC00003", "", "2024-02-10 09:30:00", "Deposit", 1000.00, "EUR", "Completed"],
    ["TXN00014", "ACC00003", 7, "2024-02-15 12:00:00", "Purchase", 320.00, "EUR", "Completed"],
    ["TXN00015", "ACC00003", "", "2024-02-20 15:30:00", "Transfer", 250.00, "USD", "Completed"],

    ["TXN00016", "ACC00004", 6, "2024-02-03 13:40:00", "Purchase", 149.99, "EUR", "Completed"],
    ["TXN00017", "ACC00004", 5, "2024-02-09 16:20:00", "Purchase", 78.50, "EUR", "Completed"],
    ["TXN00018", "ACC00004", "", "2024-02-12 10:15:00", "Deposit", 500.00, "EUR", "Completed"],
    ["TXN00019", "ACC00004", 12, "2024-02-18 11:30:00", "Purchase", 54.75, "EUR", "Pending"],
    ["TXN00020", "ACC00004", "", "2024-02-25 14:00:00", "Withdrawal", 75.00, "EUR", "Completed"],

    ["TXN00021", "ACC00005", 13, "2024-03-01 15:10:00", "Purchase", 215.00, "EUR", "Completed"],
    ["TXN00022", "ACC00005", 9, "2024-03-04 20:00:00", "Purchase", 16.50, "EUR", "Completed"],
    ["TXN00023", "ACC00005", "", "2024-03-08 09:00:00", "Deposit", 1200.00, "EUR", "Completed"],
    ["TXN00024", "ACC00005", 3, "2024-03-12 18:45:00", "Purchase", 42.00, "EUR", "Completed"],
    ["TXN00025", "ACC00005", "", "2024-03-18 12:15:00", "Direct Debit", 95.00, "EUR", "Completed"],

    ["TXN00026", "ACC00006", 1, "2024-03-02 10:30:00", "Purchase", 105.40, "EUR", "Completed"],
    ["TXN00027", "ACC00006", 4, "2024-03-06 08:10:00", "Purchase", 62.00, "EUR", "Completed"],
    ["TXN00028", "ACC00006", "", "2024-03-10 09:20:00", "Deposit", 1500.00, "EUR", "Completed"],
    ["TXN00029", "ACC00006", "", "2024-03-15 16:00:00", "Withdrawal", 200.00, "EUR", "Completed"],
    ["TXN00030", "ACC00006", 11, "2024-03-22 07:45:00", "Purchase", 12.80, "EUR", "Failed"],

    ["TXN00031", "ACC00007", 7, "2024-04-01 13:15:00", "Purchase", 450.00, "GBP", "Completed"],
    ["TXN00032", "ACC00007", 6, "2024-04-05 14:20:00", "Purchase", 189.00, "EUR", "Completed"],
    ["TXN00033", "ACC00007", "", "2024-04-10 09:30:00", "Deposit", 2000.00, "EUR", "Completed"],
    ["TXN00034", "ACC00007", "", "2024-04-15 11:45:00", "Transfer", 500.00, "EUR", "Completed"],
    ["TXN00035", "ACC00007", 10, "2024-04-20 17:30:00", "Purchase", 65.99, "EUR", "Completed"],

    ["TXN00036", "ACC00009", 2, "2024-04-02 10:00:00", "Purchase", 58.25, "EUR", "Completed"],
    ["TXN00037", "ACC00009", 3, "2024-04-08 19:15:00", "Purchase", 27.50, "EUR", "Completed"],
    ["TXN00038", "ACC00009", "", "2024-04-12 08:30:00", "Deposit", 800.00, "EUR", "Completed"],
    ["TXN00039", "ACC00009", 8, "2024-04-18 15:40:00", "Purchase", 34.95, "EUR", "Completed"],
    ["TXN00040", "ACC00009", "", "2024-04-25 12:00:00", "Withdrawal", 50.00, "EUR", "Completed"],

    ["TXN00041", "ACC00010", 14, "2024-05-01 11:20:00", "Purchase", 120.00, "EUR", "Completed"],
    ["TXN00042", "ACC00010", 15, "2024-05-05 16:45:00", "Purchase", 35.75, "EUR", "Completed"],
    ["TXN00043", "ACC00010", "", "2024-05-10 09:15:00", "Deposit", 900.00, "EUR", "Completed"],
    ["TXN00044", "ACC00010", 1, "2024-05-15 10:30:00", "Purchase", 75.60, "CHF", "Completed"],
    ["TXN00045", "ACC00010", "", "2024-05-20 14:00:00", "Direct Debit", 110.00, "EUR", "Completed"],

    ["TXN00046", "ACC00012", 5, "2024-05-03 13:00:00", "Purchase", 95.00, "EUR", "Completed"],
    ["TXN00047", "ACC00012", 9, "2024-05-08 20:15:00", "Purchase", 22.50, "EUR", "Completed"],
    ["TXN00048", "ACC00012", "", "2024-05-12 09:00:00", "Deposit", 600.00, "EUR", "Completed"],
    ["TXN00049", "ACC00013", 7, "2024-05-18 12:30:00", "Purchase", 275.00, "EUR", "Completed"],
    ["TXN00050", "ACC00015", 10, "2024-05-22 18:00:00", "Purchase", 49.95, "EUR", "Completed"]
]

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "transaction_id",
        "account_id",
        "merchant_id",
        "transaction_date",
        "transaction_type",
        "amount",
        "currency_code",
        "status"
    ])

    writer.writerows(transactions)