"""Turn your filled volumes-template.csv (e.g. from Google Keyword Planner / Semrush / Ahrefs)
into www/volumes.json that the app reads. Usage: python csv_to_json.py volumes-template.csv"""
import csv,json,sys
out={}
for row in csv.DictReader(open(sys.argv[1] if len(sys.argv)>1 else 'volumes-template.csv',encoding='utf-8')):
    vals=[row[m].replace(',','').strip() for m in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']]
    if all(v for v in vals): out[row['park']]=[int(float(v)) for v in vals]
json.dump(out,open('www/volumes.json','w'),ensure_ascii=False)
print(len(out),'parks written to www/volumes.json')
