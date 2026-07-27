import httpx
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
for url in ['https://data-asg.goldprice.org/dbXRates/USD','https://data-asg.goldprice.org/dbXRates/EUR','https://data-asg.goldprice.org/dbXRates/GBP']:
    print('URL:', url)
    try:
        r = httpx.get(url, headers=headers, timeout=20.0)
        print('status', r.status_code)
        print(r.text[:500])
    except Exception as e:
        print('ERROR', type(e).__name__, e)
    print('-'*80)
