# -*- coding: utf-8 -*-

from echarts import (
    Echart, Axis, Legend, Tooltip, Toolbox
)
from echarts.datastructure import VERSION_ALL
from nose.tools import raises


def test_axis():
    chart = Echart('Axis', 'Proportion of Browser')
    assert len(chart.json['xAxis'][0]) == 0
    assert len(chart.json['yAxis'][0]) == 0
    chart.use(Axis('category', 'bottom', 'proportion', inverse=True))
    assert chart.json['xAxis']
    chart.use(Axis('category', 'left', 'proportion', inverse=True))
    assert chart.json['yAxis']
    map(repr, chart.x_axis)


@raises(AssertionError)
def test_axis_assert_type():
    Axis('nil', 'bottom', 'proportion', inverse=True)


@raises(AssertionError)
def test_axis_assert_position():
    Axis('cetegory', 'nil', 'proportion', inverse=True)


def test_legend():
    chart = Echart('Legend', 'Demo for legend')
    chart.use(Legend(['Item1 Title'], 'vertical', show=True))

    assert chart.json['legend']['data']


@raises(AssertionError)
def test_legend_assert_position():
    Axis('cetegory', 'nil', 'proportion', inverse=True)


def test_tooltip():
    chart = Echart('Tooltip', 'Tooltip for echarts')
    chart.use(Tooltip('axis', show=True))

    assert chart.json['tooltip']['trigger'] == 'axis'
    assert chart.json['tooltip']['show'] == True


@raises(AssertionError)
def test_tooltip_assert():
    tooltip = Tooltip('nil')


def test_toolbox():
    chart = Echart('Toolbox', 'Tooltip for echarts')
    chart.use(Toolbox('horizontal', show=True))

    assert chart.json['toolbox']['orient'] == 'horizontal'
    assert chart.json['toolbox']['show'] == True


@raises(AssertionError)
def test_toolbox_assert():
    Toolbox('nil')


def test_datastructure():
    for DS in VERSION_ALL:
        chart = Echart('GDP', 'This is a fake chart')
        chart.use(DS('2014', [2, 3, 4, 5], zlevel=0))
        assert len(chart.json['series']) > 0


@raises(NotImplementedError)
def test_extra():
    str(Echart.__base__())
