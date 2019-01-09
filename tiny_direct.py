from flask import Flask, redirect
from flask import request

app = Flask(__name__)

_github = 'https://www.github.com/'
_semal = _github + 'semal259/'
_charles = _github + 'acharles7/'

SEMAL = {
    'root' : _semal,
    'a' : _semal + 'SnapNotes',
    'b' : _semal + 'vagabond',
    'c' : _semal + 'Twitterty'
}

CHARLES = {
    'root': _charles,
    'a': _charles + 'Twitterty'
}

@app.route('/<path>')
def root(path):
    if path[0] == 'S' or path[0] == 's':
        print("semal")
        try:
            if path[1] in SEMAL:
                return redirect(SEMAL[path[1]], code=302)
        except IndexError:
            print("semal index")
            return redirect(SEMAL['root'], code=302)
    elif path[0] == 'C' or path[0] == 'c':
        try:
            print("charles")
            if path[1] in CHARLES:
                return redirect(CHARLES[path[1]], code=302)
        except IndexError:
            return redirect(CHARLES['root'], code=302)
    else:
        return redirect(_github, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
