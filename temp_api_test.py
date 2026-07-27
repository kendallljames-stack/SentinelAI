import httpx
urls = {
    'goldprice': 'https://data-asg.goldprice.org/dbXRates/USD',
    'gold_silver_metals_live': 'https://api.metals.live/v1/spot/gold,silver',
    'gold_silver_metals_live_http': 'http://api.metals.live/v1/spot/gold,silver',
    'er_api': 'https://open.er-api.com/v6/latest/USD',
    'frankfurter': 'https://api.frankfurter.app/latest',
    'coingecko': 'https://api.coingecko.com/api/v3/simple/price',
}
for name, url in urls.items():
    print('===', name, url)
    try:
        if name == 'coingecko':
            r = httpx.get(url, params={'ids':'bitcoin,ethereum,monero','vs_currencies':'usd,gbp'})
        else:
            r = httpx.get(url)
        print('status', r.status_code)
        print(r.text[:500])
    except Exception as e:
        print('ERROR', type(e).__name__, e)
    print('-' * 80)
