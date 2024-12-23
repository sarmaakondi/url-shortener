from flask import Flask, request, redirect

app = Flask(__name__)

next_url_path = 0
url_mappings = {}


@app.post("/shorten")
def create_new_short_url():
    global next_url_path
    long_url = request.json["url"]
    short_url = f"/s/{next_url_path}"
    next_url_path += 1
    url_mappings[short_url] = long_url

    return short_url


if __name__ == "__main__":
    app.run(debug=True)
