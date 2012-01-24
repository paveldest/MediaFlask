from flask import Flask, render_template, abort, send_from_directory,make_response,send_file
from jinja2 import TemplateNotFound
from flaskext.lesscss import lesscss

app = Flask(__name__)

from flaskext.lesscss import lesscss
lesscss(app)

app.run

app=Flask(__name__, static_path='/static')
@app.route('/', defaults={'page': 'index'})
@app.route('/<page>')
def flask_geekmeet(page=None):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    if (app.debug):
        app.run(host='192.168.96.128', port=8080)