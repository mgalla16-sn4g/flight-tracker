from flask import Flask
from google.cloud import storage
import pandas as pd
import os
from traffic.data import opensky

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
	return f"Hello World"

@app.route("/refresh")
def refresh():
	df = opensky.api_states().data
	storage_client = storage.Client()
	bucket = storage_client.bucket('flight-data-test')
	blob = bucket.blob('test_data.json')
	blob.upload_from_string(df.to_json(), 'text/json')
	return "Success!"


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8080)