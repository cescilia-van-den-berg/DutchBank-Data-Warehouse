import subprocess
import sys
from pathlib import Path

python_folder = Path(__file__).parent

scripts = [
    "generate_customers.py",
    "generate_branches.py",
    "generate_currencies.py",
    "generate_merchants.py",
    "generate_accounts.py",
    "generate_transactions.py"
]

for script in scripts:
    script_path = python_folder / script

    print(f"Running {script}...")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=python_folder,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error while running {script}:")
        print(result.stderr)
        sys.exit(1)

print("All data generation scripts completed successfully.")