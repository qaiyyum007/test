import pandas as pd

og = pd.read_csv('OG_OD.csv', on_bad_lines='skip')
retain = pd.read_csv('soretain1.csv')

og['PlacedOn'] = pd.to_datetime(og['PlacedOn'], errors='coerce')
retain['timestamp'] = pd.to_datetime(retain['timestamp'], errors='coerce')

def check(row):
    matches = og[(og['Customer'] == row['CustomerID']) & (og['PlacedOn'] >= row['timestamp'])]
    return 'Yes' if not matches.empty else 'No'

retain['Result'] = retain.apply(check, axis=1)
retain.to_csv('output.csv', index=False)
print("Output saved to output.csv")

