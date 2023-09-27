"""
This is the main python file
"""

import pandas as pd
import json
import os

folder_path = 'data/massive'
dfs = []
for filename in os.listdir(folder_path):
    
    file_path = os.path.join(folder_path, filename)
    df = pd.read_json(file_path,orient='records',lines=True)
    dfs.append(df)

print(f'{len(dfs)} files have been converted')

dataframes = []

for index in range(len(dfs)):
    for filename in os.listdir(folder_path):

        testdata = {
        'id': dfs[10]['id'],
        'en-utt': dfs[10]['utt'],
        f'{filename[:2]}-utt': dfs[index]['utt'],
        'en-annot_utt':dfs[10]['annot_utt'],
        f'{filename[:2]}-annot_utt':dfs[index]['annot_utt']
        }

        dframe = pd.DataFrame(testdata)
        dframe.to_excel(f"excel/en-{filename[:2]}.xlsx")


