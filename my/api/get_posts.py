import json

def handler(req, res):
    try:
        with open("posts.json", "r") as f:
            data = json.load(f)
        return res.json(data)
    except Exception as e:
        return res.status(500).send(str(e))
