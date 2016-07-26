import methods
import os
from flask import Flask, request, jsonify 
app = Flask(__name__)

port = 8080

app.debug = True

@app.route("/")
def hello():
  return "Katelin Rocks!"

@app.route("/<bucket_name>/<filename>", methods=['GET', 'POST'])
def function1(bucket_name, filename):
  if request.method == 'GET':
    return methods.getFunction(bucket_name, filename)
  elif request.method == 'POST':
    payload = request.get_json()
    return methods.postFunction(bucket_name, filename, payload)
  else: 
    return "Invalid"
    


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=port)
