import httpx
ids=[]
with httpx.Client(timeout=20.0) as client:
    r=client.get('https://api.coingecko.com/api/v3/coins/list')
    coins=r.json()
    for c in coins:
        if 'silver' in c['name'].lower() or 'silver' in c['symbol'].lower():
            ids.append(c)
print('FOUND', len(ids), 'silver matches')
for item in ids[:30]:
    print(item)
