import os
import random
from pathlib import Path
from flask import Flask, request, render_template


APP_ROOT = Path(os.path.realpath(os.path.expanduser(__file__))).parents[0]
app = Flask(__name__)


with open(APP_ROOT / 'phrases.txt', 'r') as f:
    fortunes = [fortune.strip() for fortune in f]


@app.route('/')
def index():
    fortune = random.choice(fortunes).splitlines()
    chunks = []
    for line in fortune:
        _words = line.split()
        _chunk = ''
        for idx, word in enumerate(_words):
            if len(word) + len(_chunk) > 37:
                _chunk = _chunk.lstrip()
                _chunk = _chunk + ' ' * (38 - len(_chunk))
                chunks.append(_chunk)

            if idx == (len(_words) - 1):
                _chunk = ' '.join([_chunk, word])
                _chunk = _chunk.lstrip()
                _chunk = _chunk + ' ' * (38 - len(_chunk))
                chunks.append(_chunk)
            else:
                _chunk = ' '.join([_chunk, word])

    if len(chunks) == 1:
        chunks[0] = '< ' + chunks[0] + ' >'
    else:
        for idx, chunk in enumerate(chunks[1:-1]):
            chunks[idx + 1] = '| ' + chunk + ' |'
        chunks[0] = '/ ' + chunks[0] + ' \\'
        chunks[-1] = '\\ ' + chunks[-1] + ' /'
    chunks = '\n'.join(chunks)

    return render_template('index.html', fortune=chunks)


if __name__ == '__main__':
    app.run(host='127.0.0.1')
