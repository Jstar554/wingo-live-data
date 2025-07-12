import requests, json, datetime

API = "https://api.66lottery20.com/api/game/periods?game_id=9&size=1000&page=1"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    res = requests.get(API, headers=headers, timeout=10)
    data = res.json()
    result = []
    for item in data.get("data", []):
        num = int(item.get("number", 0))
        result.append({
            "period": item.get("period"),
            "number": num,
            "bigsmall": "Big" if num >= 5 else "Small",
            "color": item.get("color", "")
        })

    with open("data.json", "w") as f:
        json.dump({
            "updated": datetime.datetime.utcnow().isoformat() + "Z",
            "records": result
        }, f, indent=2)
    print("✅ data.json updated, total:", len(result))
except Exception as e:
    print("❌ scrape error:", e)
