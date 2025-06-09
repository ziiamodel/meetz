import json
from urllib.parse import parse_qs

def handler(req, res):
    if req.method == "DELETE":
        try:
            query = parse_qs(req.url.split("?", 1)[1] if "?" in req.url else "")
            index = int(query.get("index", [0])[0])

            with open("posts.json", "r+") as f:
                data = json.load(f)
                if 0 <= index < len(data):
                    data.pop(index)
                    f.seek(0)
                    json.dump(data, f, indent=2)
                    f.truncate()
            return res.json({"success": True})
        except Exception as e:
            return res.status(500).send(str(e))
    else:
        return res.status(405).send("Method not allowed")
