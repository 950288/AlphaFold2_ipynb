import json

with open('KMCR.fa') as f:
    lines = f.readlines()

results = []
seq = ''
results.append({})
for line in lines:
    if line.startswith('>'):
        if seq:
            results[len(results) - 1]['sequence'] = seq   
            results.append({})
        headers = line.strip().split(', ')
        for header in headers:
            try:
                k, v = header.split('=')
                results[len(results) - 1][k] = v
            except ValueError:
                results[len(results) - 1]["sample"] = "origin"
        seq = ''
    else:
        seq += line.strip()

if seq:
    results[len(results) - 1]['sequence'] = seq

with open('KMCR.json', 'w') as f:
    json.dump(results, f)
