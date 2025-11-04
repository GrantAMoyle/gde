from flask import Flask, request
from waitress import serve
from faker import Faker
import os
import logging
import random
import usegemini

app = Flask(__name__)
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)
fake = Faker()

# Using Gemini, return a random piece of information about Oregon State University ondemand
@app.route("/osu")
def getOSUInfo():
  osu_facts = [
      "Oregon State University is located in Corvallis, Oregon.",
      "The mascot of Oregon State University is the Beaver, and its name is Benny the Beaver.",
      "Oregon State University is a leading research institution, particularly in areas like oceanography, forestry, and agricultural sciences.",
      "The university was founded in 1868.",
      "Oregon State University is one of only two universities in the U.S. to have Sea Grant, Space Grant, and Sun Grant designations.",
      "The official colors of Oregon State University are orange and black.",
      "Oregon State University has a strong engineering program.",
      "The university offers over 200 undergraduate and 100 graduate degree programs.",
      "Oregon State University is known for its beautiful campus and vibrant student life.",
      "The university has a significant impact on the state's economy and workforce."
  ]
  return usegemini.generate()
  #return random.choice(osu_facts)
  
@app.route("/")
def getRoot():
  return "Welcome OSU!\n"

@app.route("/headers")
def show_headers():
  client_ip = request.remote_addr
  user_agent = request.headers.get('User-Agent')
  referer = request.headers.get('Referer')
  accept_language = request.headers.get('Accept-Language')
  all_headers = dict(request.headers)
  header_info = f"Your IP address is: {client_ip}<br\>" \
                f"Headers: {all_headers}"
  return header_info

@app.route("/random")
def getRandom():
  randomnum = random.randint(1, 100000000)/100
  return "Your Random Number is " + str(randomnum) + "!\n"

@app.route("/name")
def getRandomName():
  randomname = "Welcome " + fake.name()
  return randomname

@app.route("/version")
def version():
  return "ROI Training Demo 1.0\n"



if __name__ == "__main__":
  serve(app,host="0.0.0.0",port=int(os.environ.get("PORT", 8080)))
