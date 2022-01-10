
import json
import csv
import os
 
headers = ['item','country','year','sales']

path_csv = f'./sales.csv'
with open(path_csv,'a+', newline='') as csvfile:
    spawnrow = csv.DictWriter(csvfile, fieldnames=headers)
    spawnrow.writeheader()
with open(f'./sales.json') as f:
    tmp = json.load(f)
with open(path_csv, 'a+', newline='') as csvfile:
    spawnrow = csv.DictWriter(csvfile, fieldnames=headers)
    for item in tmp:
        countrys = item["sales_by_country"]
        for country in countrys:
            years = countrys[country]
            for year in years:
                spawnrow.writerow(
                    {'item': f'{item["item"]}', 'country': f'{country}',
                    'year': f'{year}', 'sales': f'{years[year]}'})
