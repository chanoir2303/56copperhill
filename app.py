from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)


@app.route('/')
def index():
    title = '56 Copperhill'
    return render_template('index.html', title=title)


@app.route('/form', methods=['POST'])
def form():
    choice = request.form.get('choice')
    name = request.form.get('name')
    comments = request.form.get('comments')

    message = f'{choice} / {name} / {comments}'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('56copperhill@gmail.com', 'azertyytreza')
    server.sendmail('56copperhill@gmail.com', 'kvnselen@icloud.com', message)

    title = 'Order sent'

    return render_template('return.html', title=title)


if __name__ == '__main__':
    app.run()
