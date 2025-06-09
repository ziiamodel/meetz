import json

def handler(req, res):
    if req.method == "POST":
        try:
            new_post = req.json()
            with open("posts.json", "r+") as f:
                data = json.load(f)
                data.insert(0, new_post)
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
            return res.json({"success": True})
        except Exception as e:
            return res.status(500).send(str(e))
    else:
        return res.status(405).send("Method not allowed")
