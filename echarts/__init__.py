# coding: utf-8

from .datastructure import *
from .option import Axis, Legend, Tooltip, Series, Toolbox
from .option import Base

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
        elif isinstance(obj, Toolbox):
            self.toolbox = obj

        return self

    @property
    def data(self):
        return self.series

    @property
    def json(self):
        """JSON format data."""
        json = {
            'title': self.title,
            'series': list(map(dict, self.series)),
        }
        if self.x_axis:
            json['xAxis'] = list(map(dict, self.x_axis))
        if self.y_axis:
            json['yAxis'] = list(map(dict, self.y_axis))

        if not hasattr(self, 'legend'):
            self.legend = Legend(list(map(lambda o: o.name, self.data)))

        json['legend'] = self.legend.json

        if hasattr(self, 'tooltip'):
            json['tooltip'] = self.tooltip.json
        if hasattr(self, 'toolbox'):
            json['toolbox'] = self.toolbox.json

        return json
