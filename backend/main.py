"""
/ -> url [BUT] -> back -> db -> short url
/short_url -> front -> back -> db [url] -> front redirect


"""

from flask import Flask, jsonify, redirect, request, abort
from flask_cors import CORS
import string
import random
from urllib.parse import urljoin
import db
import config


app = Flask(__name__)
CORS(app)


def new_page_name() -> str:
    while True:
        short_url = ''.join(
            random.choices(string.ascii_letters+string.digits, k=6)
        )
        if db.get_url(short_url) is None:
            break
    return short_url


def _using_cors(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    url = request.json['url']
    key = new_page_name()
    db.put_url(key, url)
    short_url = urljoin(config.site_domain, 'u/' + key)
    return _using_cors(jsonify({'url': short_url}))


@app.route('/u/<path:url>', methods=['GET'])
def get(url):
    print(f'ask to redirect from {url!r}')
    target_url = db.get_url(url)
    if target_url is None:
        abort(404)
    return _using_cors(redirect(target_url))


if __name__ == '__main__':
   app.run('0.0.0.0', 5000)

    