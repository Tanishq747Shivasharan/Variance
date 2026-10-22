
import pandas as pd
from pathlib import Path


file_path = Path(
    r"C:\Users\ankit\Variance-full-backup\The_SEERA_Dataset\The SEERA Dataset\Dataset Files\SEERA dataset original raw data.xlsx"
)

if file_path.exists():
    print("Dataset found successfully!")

    excel = pd.ExcelFile(file_path)
    print("\nAvailable sheets:")
    print(excel.sheet_names)

else:
    print("Dataset not found!")
    print("Checked path:", file_path)
