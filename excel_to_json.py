import pandas as pd

excel_file = "enti_strutture.xlsx"
json_file = "enti_strutture.json"

df = pd.read_excel(excel_file)
df.to_json(json_file, orient="records", indent=2, force_ascii=False)

print(f"✅ File JSON aggiornato: {json_file}")
