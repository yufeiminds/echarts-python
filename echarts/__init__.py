# coding: utf-8

from .option import Base
from .option import Axis, Legend, Tooltip, Series


class Echart(Base):
    def __init__(self, title, description=None):
        self.title = {
            'text': title,
            'subtext': description,
        }

        self.x_axis = []
        self.y_axis = []
        self.series = []

    def use(self, data):
        if isinstance(data, Axis):
            if data.position in ('bottom', 'top'):
                self.x_axis.append(data)
            else:
                self.y_axis.append(data)
            return self

        if isinstance(data, Legend):
            self.legend = data
        elif isinstance(data, Tooltip):
            self.tooltip = data
        elif isinstance(data, Series):
            self.series.append(data)

        return self

    @property
    def data(self):
        return self.series

    @property
    def json(self):
        """JSON format data."""
        json = {
            'title': self.title,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
            'series': self.series,
        }

        if not hasattr(self, 'legend'):
            self.legend = Legend(map(lambda o: o.name, self.data))

        json['legend'] = self.legend.json

        if hasattr(self, 'tooltip'):
            json['tooltip'] = self.tooltip.json

        return json

    @classmethod
    def create_from_data_frame(cls, df):
        """Create an echart from pandas DataFrame."""
