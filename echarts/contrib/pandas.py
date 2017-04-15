# -*- coding: utf-8 -*-

"""
    echarts.contrib.pandas
    ~~~~~~~~~~~~~~~~~~~~~~

    contribution package for pandas
"""

from echarts import Echart, Line, Legend, Axis


def from_df(df,
            types=None,
            title=None,
            description=None,
            legends=None):
    """ load chart from pandas dataframe

    >>> import pandas as pd
    >>> df = pd.DataFrame.from_records([
    >>>     {'value': 1},
    >>>     {'value': 2},
    >>>     {'value': 3}
    >>> ])
    >>> from_df(df=df, title=u'Testing Chart', description=u'')

    :param df: pandas Dataframe or Dataframe-like object
    :return: Echart object
    """
    chart = Echart(title=title, description=description)

    for key, legend in zip(df.keys(), legends or df.keys()):
        chart.use(Line(legend, list(df[key])))

    # Legends list
    chart.use(
        Legend(legends or list(df.keys()))
    )

    # Axis
    chart.use(Axis('category', 'bottom', data=range(0, len(df.index))))
    return chart
