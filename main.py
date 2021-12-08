"""
/ -> url [BUT] -> back -> db -> short url
/short_url -> front -> back -> db [url] -> front redirect


"""

from flask import Flask, jsonify, redirect, request, abort
import string
import random
from urllib.parse import urljoin
import db
import config


app = Flask(__name__)

def new_page_name() -> str:
    while True:
        short_url = random.choices((string.ascii_letters, string.digits), k=6)
        if db.get_url(short_url) is None:
            break


@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    url = request.json['url']
    short_url = urljoin(config.site_domain, new_page_name())
    db.put_url(short_url, url)
    return jsonify({'url': short_url})


@app.route('/<path:url>', methods=['GET'])
def get(url):
    print(f'ask to redirect from {url!r}')
    target_url = db.get_url(url)
    if target_url is None:
        abort(404)
    return redirect(target_url)


if __name__ == '__main__':
   app.run()

    