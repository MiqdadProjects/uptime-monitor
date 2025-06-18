import requests, time, json

URLS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.youtube.com",
    "http://example.invalid"
]

def check_site(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()
        return {
            "url": url,
            "status": "up",
            "code": response.status_code,
            "response_time": round(end - start, 2)
        }
    except:
        return {
            "url": url,
            "status": "down",
            "code": None,
            "response_time": None
        }

def check_all_sites():
    results = [check_site(url) for url in URLS]
    with open("db.json", "w") as f:
        json.dump(results, f, indent=2)
    return results
