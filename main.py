from bokeh.models.widgets import TextInput, Button
from bokeh.plotting import curdoc
from google.cloud import storage
import logging
from modules import *
import numpy as np
import pandas as pd
from utils import config
from utils.df_operations import wgs84_to_web_mercator, degrees_to_rads

_logger = logging.getLogger(__name__)
client = storage.Client()
configs = config.settings
modules = [big_map.Module(), data_table.Module()]
filter_vals = []

def fetch_data():
	bucket = client.get_bucket(configs['bucket-name'])
	blob = bucket.get_blob(configs['object-name'])
	df = pd.read_json(blob.download_as_string())
	df = wgs84_to_web_mercator(df)
	df = degrees_to_rads(df)
	if filter_vals and '' not in filter_vals:
		filtered = df.loc[df['callsign'].isin(filter_vals)]
		return filtered
	return df

def update():
	for module in modules:
		getattr(module, 'busy')()
	results = fetch_data()
	for module in modules:
		getattr(module, 'update_plot')(results)
	for module in modules:
		getattr(module, 'unbusy')()

def search_callsigns(attr, old, new):
	filter_vals.append(new)
	update()

def clear_filters():
	filter_vals = []
	text_input.value = ""
	update()

results = fetch_data()

for module in modules:
	block = getattr(module, 'make_plot')(results)
	curdoc().add_root(block)

## Create Filter Text Box and Clear Button
text_input = TextInput(title = "Search for a Callsign:", name = "textin", placeholder="Search...")
text_input.on_change('value', search_callsigns)

clear_button = Button(label = "Clear Filters", name = "clear")
clear_button.on_click(clear_filters)

curdoc().title = configs['index-title']
curdoc().add_root(text_input)
curdoc().add_root(clear_button)
curdoc().add_periodic_callback(update, configs['callback-period'])
