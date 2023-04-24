from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/saudacao')
def saudacao():
    return render_template('saudacao.html')

if __name__ == '__main__':
    app.run()