# -*- coding: utf-8 -*-

"""
    echarts
    ~~~~~~~

    An unofficial Echarts options generator with Python.

    :copyright: (c) 2014 by Hsiaoming Yang <me@lepture.com>.
    :license: MIT, see `MIT <https://opensource.org/licenses/MIT>`_ for more details.
"""

import os
import json
import logging
import tempfile
import webbrowser
from .option import Base
from .option import Axis, Legend, Series, Tooltip, Toolbox
from .datastructure import *

__version__ = '0.1'
__release__ = '0.1.2'
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

        self.logger = logging.getLogger(__name__)

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
            'xAxis': list(map(dict, self.x_axis)) or {},
            'yAxis': list(map(dict, self.y_axis)) or {},
            'series': list(map(dict, self.series)),
        }

        if not hasattr(self, 'legend'):
            self.legend = Legend(list(map(lambda o: o.name, self.data)))

        json['legend'] = self.legend.json

        if hasattr(self, 'tooltip'):
            json['tooltip'] = self.tooltip.json
        if hasattr(self, 'toolbox'):
            json['toolbox'] = self.toolbox.json

        return json

    def plot(self):
        html = tempfile.NamedTemporaryFile(suffix='.html', delete=False)
        with open(os.path.join(os.path.dirname(__file__), 'plot.j2')) as f:
            template = f.read()
            content = template.replace('{{ opt }}', json.dumps(self.json, indent=4))
            html.write(content)
        webbrowser.open('file://' + os.path.realpath(html.name))
        html.close()
