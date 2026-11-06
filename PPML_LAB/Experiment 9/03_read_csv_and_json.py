# Program 3: Read CSV and JSON files using Pandas
import pandas as pd

# The sample files are created here so the program runs independently.
csv_data = pd.DataFrame({"Name": ["Asha", "Bina", "Chetan"], "Marks": [85, 90, 78]})
csv_data.to_csv("sample.csv", index=False)
json_data = pd.DataFrame({"Name": ["Asha", "Bina", "Chetan"], "City": ["Gunupur", "Rayagada", "Berhampur"]})
json_data.to_json("sample.json", orient="records", indent=4)

print("Data read from CSV file:")
print(pd.read_csv("sample.csv"))
print("\nData read from JSON file:")
print(pd.read_json("sample.json"))
