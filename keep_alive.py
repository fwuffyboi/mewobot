from flask import Flask
from threading import Thread
import random


numcount = 0 

app = Flask('')

@app.route('/')
def home():
	return 'online, check https://uptimerobot.com/dashboard.php for more information'
	
	
def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()