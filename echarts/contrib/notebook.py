# -*- coding: utf-8 -*-

"""
    
    ~~~~~~~


"""

import json
from IPython.display import HTML


def plot(chart, width='800px', height='600px'):
    return HTML('''
    <div id="chart"
         style="width: ''' + width + '''; height: ''' + height + ''';">
    </div>

    <script>
        require.config({
            paths: {
                echarts: '//cdn.bootcss.com/echarts/3.5.0/echarts.min'
            }
        });
        require(['echarts'], function(ec) {
            var chart = ec.init(document.getElementById('chart'));
            chart.setOption(''' + json.dumps(chart.json) + ''');
        });
    </script>
    ''')
