
from echarts import Echart, Bar


def test_bar():
    chart = Echart('GDP', 'This is a fake chart')
    chart.use(Bar(2014, [2, 3, 4, 5]))
    print(str(chart))
