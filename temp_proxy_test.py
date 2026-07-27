import httpx
urls = [
    'https://api.allorigins.win/raw?url=https://api.metals.live/v1/spot/gold,silver',
    'https://api.allorigins.win/raw?url=https://api.metals.live/v1/spot/gold',
    'https://api.allorigins.win/raw?url=https://api.metals.live/v1/spot/silver',
]
with httpx.Client(timeout=30.0) as client:
    for url in urls:
        print('URL',url)
        try:
            r=client.get(url)
            print('status', r.status_code)
            print(r.text[:600])
        except Exception as e:
            print('ERROR', type(e).__name__, e)
        print('-'*80)
