"""
/ -> url [BUT] -> back -> db -> short url
/short_url -> front -> back -> db [url] -> front redirect


"""

from flask import Flask, jsonify, redirect, request
import db


app = Flask(__name__)

@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    url = request.json['url']
    return jsonify({'url': url})


@app.route('/<path:url>', methods=['GET'])
def get(url):
    print(f'ask to redirect from {url!r}')
    # TODO: check that redirected url is not to our site (how?)
    url = 'https://google.com/'
    return redirect(url)


if __name__ == '__main__':
   app.run()

    