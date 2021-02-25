from google_trans_new import google_translator  
import convert
import json
import os

# translate script, taking the original professions list and translating them to maltese
# curating such list is required
rpath = "src\debiaswe\professions.json"
translator = google_translator()  
mt_professions = []

with open(rpath, 'r') as f:
    professions = json.load(f)

for p in professions:
    t = translator.translate(p[0], lang_tgt="mt")
    mt_professions.append([convert.maltese_to_english(t.strip()), p[1], p[2]])

with open("mt_professions.json", 'w') as f:
    json.dump(mt_professions, fp=f)