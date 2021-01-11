from datetime import datetime, timezone
import numpy as np
import pandas as pd

def wgs84_to_web_mercator(df, lon="longitude", lat="latitude"):
	    k = 6378137
	    df["x"] = df[lon] * (k * np.pi/180.0)
	    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
	    return df

def degrees_to_rads(df):
	df['heading_rad'] = df['track']*(np.pi/180)
	return df

def make_timestamps_readable(timestamp):
	return datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S.%f+00:00 (UTC)")
