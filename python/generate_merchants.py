import csv
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_file = project_root / "data" / "raw" / "merchants.csv"

merchants = [
    [1, "Albert Heijn Tilburg", "Supermarket", "Tilburg"],
    [2, "Jumbo Breda Centrum", "Supermarket", "Breda"],
    [3, "Eetcafe De Markt", "Restaurant", "Tilburg"],
    [4, "Shell Tilburg", "Fuel", "Tilburg"],
    [5, "H&M Eindhoven", "Clothing", "Eindhoven"],
    [6, "MediaMarkt Eindhoven", "Electronics", "Eindhoven"],
    [7, "Booking.com", "Travel", "Amsterdam"],
    [8, "Etos Rotterdam", "Healthcare", "Rotterdam"],
    [9, "Pathé Tilburg", "Entertainment", "Tilburg"],
    [10, "Bol.com", "Online Shopping", "Utrecht"],
    [11, "NS", "Public Transport", "Utrecht"],
    [12, "Lidl Rotterdam", "Supermarket", "Rotterdam"],
    [13, "IKEA Eindhoven", "Electronics", "Eindhoven"],
    [14, "Zalando", "Online Shopping", "Amsterdam"],
    [15, "Kruidvat Breda", "Healthcare", "Breda"]
]

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "merchant_id",
        "merchant_name",
        "merchant_category",
        "city"
    ])

    writer.writerows(merchants)