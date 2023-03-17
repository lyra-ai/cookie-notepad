from flask import Flask, request, make_response, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        response = make_response('success')
        response.set_cookie('notepad', content)
        return response
    else:
        content = request.cookies.get('notepad', '')
        return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
