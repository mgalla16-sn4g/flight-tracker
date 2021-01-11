from bokeh.models import HoverTool
from bokeh.plotting import figure, ColumnDataSource
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
from modules.base import BaseModule
from utils import config

configs = config.settings

class Module(BaseModule):

	def __init__(self):
		super().__init__()
		self.source = None
		self.plot = None
		self.title = None

	def make_plot(self, dataframe):
		self.source = ColumnDataSource(data=dataframe)
		x_r,y_r=([-15187814,-6458032], [2505715,6567666]) ## coordinates to center around the USA
		p = figure(title=configs['map-title'], x_range = x_r, y_range = y_r, x_axis_type = "mercator", y_axis_type = "mercator", name = 'plane_map', sizing_mode = 'scale_width')
		tile_provider = get_provider(CARTODBPOSITRON)
		p.add_tile(tile_provider)
		my_hover=HoverTool()
		my_hover.tooltips=[('Callsign','@callsign'),('Altitude','@geoaltitude')]
		p.add_tools(my_hover)
		p.triangle('x', 'y', source = self.source, fill_color = "blue", size = 10, fill_alpha = 0.8, line_width=0.5, angle = 'heading_rad')
		self.plot = p
		return self.plot

	def update_plot(self, dataframe):
		self.source.data.update(dataframe)

	def busy(self):
		self.plot.title.text = 'Updating...'

	def unbusy(self):
		self.plot.title.text = configs['map-title']