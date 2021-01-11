from bokeh.models import HoverTool
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.plotting import figure, ColumnDataSource
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
from modules.base import BaseModule
from utils import config

configs = config.settings

class Module(BaseModule):

	def __init__(self):
		super().__init__()
		self.source = None
		self.table = None
		self.title = None

	def make_plot(self, dataframe):
		self.source = ColumnDataSource(data=dataframe)
		columns = [TableColumn(field = i, title = i.replace("_"," ").title()) for i in list(dataframe.drop(configs['dropped-columns'], axis=1).round(1).columns)]
		self.table = DataTable(source = self.source, columns = columns, name = "data_table",  index_position = None, fit_columns = True)
		return self.table

	def update_plot(self, dataframe):
		self.source.data.update(dataframe)

	def busy(self):
		pass

	def unbusy(self):
		pass