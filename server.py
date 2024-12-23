import random
import string
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)


class URLShortener:
    def __init__(self, shortened_length=8):
        self.shortened_length = shortened_length
        self.url_mappings = {}

    def generate_short_url(self):
        """Generate a unique short URL."""
        while True:
            short_url = "".join(
                random.choices(string.ascii_lowercase, k=self.shortened_length)
            )
            if short_url not in self.url_mappings:
                return short_url

    def add_mapping(self, long_url):
        """Creates a mapping from a long URL to a short URL."""
        short_url = self.generate_short_url()
        self.url_mappings[short_url] = long_url
        return short_url

    def get_long_url(self, short_url):
        """Retrieves the long URL associated with a short URL."""
        return self.url_mappings.get(short_url)


# Initialize the URL shortener
url_shortener = URLShortener()


# Routes
@app.post("/shorten")
def create_new_short_url():
    """Endpoint to shorten a URL."""
    data = request.json
    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' field"}), 400

    long_url = data["url"]
    short_url = url_shortener.add_mapping(long_url)
    return jsonify({"short_url": f"/s/{short_url}"})


@app.get("/s/<short_url>")
def redirect_to_url(short_url):
    """Endpoint to redirect to the long URL."""
    long_url = url_shortener.get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    return jsonify({"error": "URL not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
