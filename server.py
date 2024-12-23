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


if __name__ == "__main__":
    app.run(debug=True)
