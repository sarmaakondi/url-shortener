import random
import string
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)


class URLShortener:
    def __init__(self, short_url_length=8):
        """Initialize with a default short URL length of 8 characters."""
        self.short_url_length = short_url_length
        self.url_map = {}

    def generate_unique_short_url(self):
        """Generate a unique short URL."""
        while True:
            short_url = "".join(
                random.choices(string.ascii_lowercase, k=self.short_url_length)
            )
            if short_url not in self.url_map:
                return short_url

    def create_short_url(self, original_url):
        """Create a short URL for a given long URL."""
        short_url = self.generate_unique_short_url()
        self.url_map[short_url] = original_url
        return short_url

    def retrieve_long_url(self, short_url):
        """Retrieve the long URL associated with a short URL."""
        return self.url_map.get(short_url)


# Initialize the URL shortener
url_shortener_service = URLShortener()


# Routes
@app.post("/shorten")
def shorten_url():
    """Endpoint to shorten a URL."""
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' field"}), 400

    long_url = data["url"]
    short_url = url_shortener_service.create_short_url(long_url)
    return jsonify({"short_url": f"/{short_url}"})


@app.get("/<short_url>")
def redirect_to_long_url(short_url):
    """Endpoint to redirect to the long URL."""
    long_url = url_shortener_service.retrieve_long_url(short_url)
    if long_url:
        return redirect(long_url)
    return jsonify({"error": "Short URL not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
