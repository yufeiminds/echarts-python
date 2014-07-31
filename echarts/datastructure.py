#coding: utf-8

import json


class Base(object):
    def __str__(self):
        """JSON stringify format data."""
        return json.dumps(self.json)

    def __dict__(self):
        return self.json

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
        assert type in ('category', 'value')
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


class Line(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Line, self).__init__('line', name=name, data=data, **kwargs)


class Bar(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Bar, self).__init__('bar', name=name, data=data, **kwargs)


class Pie(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Pie, self).__init__('pie', name=name, data=data, **kwargs)


class Scatter(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Scatter, self).__init__(
            'scatter', name=name, data=data, **kwargs
        )


class Radar(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Radar, self).__init__('radar', name=name, data=data, **kwargs)


class Force(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Force, self).__init__('force', name=name, data=data, **kwargs)


class Chord(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Chord, self).__init__('chord', name=name, data=data, **kwargs)


class Map(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Map, self).__init__('map', name=name, data=data, **kwargs)
