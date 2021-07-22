from flask import Flask
from threading import Thread

#Defines a flask server
app = Flask('')

#The home page
@app.route('/')
def home():
  return "Hello. I am alive"

#Running the server
def run():
  app.run(host='0.0.0.0', port='8080')

#Method that creates a separate thread from the bot
def keep_alive():
  t = Thread(target=run)
  t.start()