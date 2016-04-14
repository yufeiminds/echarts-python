#coding: utf-8

import json


class Base(object):
    def __str__(self):
        """JSON stringify format data."""
        return json.dumps(self.json)

    def __getitem__(self, key):
        return self.json.get(key)

    def keys(self):
        return self.json.keys()

    @property
    def json(self):
        raise NotImplementedError


class Axis(Base):
    """Axis data structure."""

    def __init__(self, type, position, name='', data=None, **kwargs):
        assert type in ('category', 'value', 'time')
        self.type = type
        assert position in ('bottom', 'top', 'left', 'right')
        self.position = position
        self.name = name
        self.data = data or []
        self._kwargs = kwargs

    def __repr__(self):
        return 'Axis<%s/%s>' % (self.type, self.position)

    @property
    def json(self):
        """JSON format data."""
        json = dict(
            type=self.type,
            position=self.position,
            data=self.data
        )
        if self.name:
            json['name'] = self.name

        if self._kwargs:
            json.update(self._kwargs)
        return json


class Legend(Base):
    """Legend section for Echart."""
    def __init__(self, data, orient='horizontal', position=None, **kwargs):
        self.data = data

        assert orient in ('horizontal', 'vertical')
        self.orient = orient
        if not position:
            position = ('center', 'top')
        self.position = position
        self._kwargs = kwargs

    @property
    def json(self):
        """JSON format data."""
        json = {
            'data': self.data,
            'orient': self.orient,
            'x': self.position[0],
            'y': self.position[1]
        }

        if self._kwargs:
            json.update(self._kwargs)
        return json


class Tooltip(Base):
    """A tooltip when hovering."""
    def __init__(self, trigger='axis', **kwargs):
        assert trigger in ('axis', 'item')
        self.trigger = trigger

        self._kwargs = kwargs

    @property
    def json(self):
        json = {
            'trigger': self.trigger,
        }
        if self._kwargs:
            json.update(self._kwargs)
        return json


class Series(Base):
    def __init__(self, type, name=None, data=None, **kwargs):
        types = (
            'line', 'bar', 'scatter', 'k', 'pie', 'radar',
            'chord', 'force', 'map'
        )
        assert type in types
        self.type = type
        self.name = name
        self.data = data or []
        self._kwargs = kwargs

    @property
    def json(self):
        json = {
            'type': self.type,
            'data': self.data
        }
        if self.name:
            json['name'] = self.name
        if self._kwargs:
            json.update(self._kwargs)
        return json


class Toolbox(Base):
    def __init__(self, show='true', orient='horizontal', position=None, **kwargs):
        assert show in ('true', 'false')
        self.show = show
        assert orient in ('horizontal', 'vertical')
        self.orient = orient
        if not position:
            position = ('right', 'top')
        self.position = position
        self._kwargs = kwargs

    @property
    def json(self):
        json = {
            'show': self.show,
            'orient': self.orient,
            'x': self.position[0],
            'y': self.position[1]
        }

        if self._kwargs:
            json.update(self._kwargs)
        return json
