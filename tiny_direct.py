from flask import Flask, redirect

app = Flask(__name__)

_github = 'https://www.github.com/'
_semal = _github + 'semal259/'
_charles = _github + 'acharles7/'

SEMAL = {
    'root': _semal,
    'a': _semal + 'SnapNotes'
}

CHARLES = {
    'root': _charles,
    'a': _charles + 'Twitterty',
    'b': _charles + 'Sentiment-Analysis',
    'c': _charles + 'Note'
}

@app.route('/test/awesome')
def test():
    return "Hi, teddy!"

@app.route('/<path>')
def root(path):
    if len(path) > 1:
        if path[0] == 'S' or 's':
            if path[1] in SEMAL:
                return redirect(SEMAL[path[1]], code=302)
            else:
                return redirect(SEMAL['root'], code=302)
        elif path[0] == 'C' or 'c':
            if path[1] in CHARLES:
                return redirect(CHARLES[path[1]], code=302)
            else:
                return redirect(CHARLES['root'], code=302)
    return redirect(_github, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
