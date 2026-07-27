import httpx

with httpx.Client(timeout=20.0) as client:
    r = client.get('https://api.coingecko.com/api/v3/coins/list')
    coins = r.json()
    names = [c for c in coins if 'gold' in c['name'].lower() or 'silver' in c['name'].lower()]
    print('found', len(names), 'matches')
    for c in names[:50]:
        print(c)
