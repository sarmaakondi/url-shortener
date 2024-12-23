# url-shortener

## Overview

This project is a simple URL shortener built with Python. It takes long URLs and generates shorter versions that redirect to the original URLs.

## Features

-   Shorten long URLs
-   Redirect short URLs to the original URLs
-   Simple and easy-to-use interface

## Requirements

-   Python 3.x
-   Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sarmaakondi/url-shortener.git
    ```
2. Navigate to the project directory:
    ```bash
    cd url-shortener
    ```
3. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the server:
    ```bash
    python server.py
    ```
2. Open Postman/HTTPie/your_favourite_app and go to `http://localhost:5000`
3. To shorten a URL, you can use the following example body:
    ```json
    {
        "url": "https://news.ycombinator.com"
    }
    ```
    The example output will be:
    ```json
    {
        "short_url": "/s/tndamkjd"
    }
    ```
4. You can access the target site using the short URL by navigating to `http://localhost:5000/s/tndamkjd`

## License

This project is licensed under the [MIT License](LICENSE).
