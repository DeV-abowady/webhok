from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)


@app.route('/')
def index():
  render_template('index.html')


if __name__ == "__main__":
  bot.polling()
  app.run(host='0.0.0.0')
