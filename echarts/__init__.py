# coding: utf-8

from .option import Base
from .option import Axis, Legend, Tooltip, Series, Toolbox
from .datastructure import *

__version__ = '0.1'
__author__ = 'Hsiaoming Yang <me@lepture.com>'


class Echart(Base):
    def __init__(self, title, description=None, **kwargs):
        self.title = {
            'text': title,
            'subtext': description,
        }

        self.x_axis = []
        self.y_axis = []
        self.series = []

    def use(self, obj):
        if isinstance(obj, Axis):
            if obj.position in ('bottom', 'top'):
                self.x_axis.append(obj)
            else:
                self.y_axis.append(obj)
            return self

        if isinstance(obj, Legend):
            self.legend = obj
        elif isinstance(obj, Tooltip):
            self.tooltip = obj
        elif isinstance(obj, Series):
            self.series.append(obj)

        return self

    @property
    def data(self):
        return self.series

    @property
    def json(self):
        """JSON format data."""
        json = {
            'title': self.title,
            'xAxis': list(map(dict, self.x_axis)),
            'yAxis': list(map(dict, self.y_axis)),
            'series': list(map(dict, self.series)),
        }

        if not hasattr(self, 'legend'):
            self.legend = Legend(list(map(lambda o: o.name, self.data)))

        json['legend'] = self.legend.json

        if hasattr(self, 'tooltip'):
            json['tooltip'] = self.tooltip.json

        return json
