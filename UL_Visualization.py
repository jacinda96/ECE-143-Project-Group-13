'''
UL_Visualization.py
author: Robert Young
'''

import pandas as pd
import matplotlib as plt


def scatter_ppm_vs_weather(df, weather, title, xaxis, color):
    '''
    Creates a "heatmap" scatterplot of price per mile vs weather condition
    df : pd.DataFrame to pull data from
    weather: the weather condition we are going to plot against
    title: string title of the graph
    xaxis: the title of the xaxis
    color: the color of the scatter markers
    '''

    assert isinstance(df, pd.DataFrame)
    assert isinstance(weather, str)
    assert isinstance(title, str)
    assert isinstance(xaxis, str)
    assert isinstance(color, str)

    plt.figure()
    plt.scatter(df[weather], (df['price'] / df['distance']), alpha=0.02, facecolor=color),
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel('Price per Mile (USD/mile)')
    plt.show()


def thresholdTime(df, target, threshold):
    '''
    Returns a subset of the original dataframe: df containing only entries
    whose value in the "time" column is the same as the target column
    df: pd.DataFrame to pull data from
    target: the target hour [0,24]
    threshold: the amount of hours ahead of the target that will be accepted for the ret data
    return: a pd.DataFrame consisting of rows that fit in the threshold from the target hour
    '''
    assert isinstance(df, pd.DataFrame)
    assert isinstance(target, int) and 0 <= target <= 24
    assert isinstance(threshold, int)

    times = df['time']
    valid = []
    for time in times:
        tsplit = time.split(':')
        thour = int(tsplit[0])
        if target - thour < threshold:
            valid.append(time)
    ret = df[df['time'].isin(valid)]

    return ret


def weekday_avgs(df):
    '''
    Returns a dataframe whose index is the integer representation of the
    days of the week and the column values the average price for that day
    df: pd.DataFrame to pull data from
    return: pd.DataFrame of the mean price per mile ordered with an index of its corresonpding weekday
    '''
    assert isinstance(df, pd.DataFrame)

    wda = df.groupby('weekday')['price'].mean() / df.groupby('weekday')['distance'].mean()

    return wda


def price_avg_vs_weekday(df, weekdays, title, start, end, interval):
    '''
    Generates a Average price vs weekday graph
    df: the dataframe to pull price data from
    weekdays : the x-axis labels
    interval: the time interval to generate the list of time plots
    start: the starting hour for the time intervals
    end: the ending time for the time intervals
    return: reference to the figure
    '''

    assert isinstance(df, pd.DataFrame)
    assert isinstance(weekdays, list)
    assert isinstance(title, str)
    assert isinstance(interval, int) and interval > 0
    assert isinstance(start, int) and start >= 0 and start <= 24
    assert isinstance(end, int) and end >= 0 and end <= 24

    fig = plt.figure()

    for i in range(start, end, interval):
        stime = '{}{}'.format(str(i if i < 12 else i - 12), ('am' if i < 12 else 'pm'))
        iend = i + interval
        etime = '{}{}'.format(str(iend if iend < 12 else iend - 12), ('am' if iend < 12 else 'pm'))
        trange = '{}-{}'.format(stime, etime)
        plt.plot(weekdays, weekday_avgs(thresholdTime(df, i, interval)), label=trange)

    plt.xlabel('Weekday')
    plt.ylabel('Avg Price per Mile (USD/mile)')
    plt.title(title)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07), fancybox=True, shadow=True, ncol=3)
    plt.grid()

    return fig


def cab_type_vs_ppm(df, cabtypes, title, color, fliers=False):
    '''
    Produces graph containing a boxplot(s) of the price
    per mile vs every cab_type for the particular df.
    The ordering of cab types follows the ordering of the cabtypes list.
    df: the dataframe to pull data from
    cabtypes: a list of string names of the cabtypes to be plotted from df in the order given
    title: a string title of the graph
    color: the color of the filling for each boxplot
    fliers: True = show outliers, False = no outliers
    return: reference to the figure plotted
    '''

    assert isinstance(df, pd.DataFrame)
    assert isinstance(cabtypes, list)
    assert isinstance(title, str)
    assert isinstance(color, str)
    assert isinstance(fliers, bool)

    ctypes = df['name'].unique().tolist()

    f = plt.figure()

    ppm_data = []
    for ctype in cabtypes:
        ppm_data.append((df[df['name'] == ctype].price / df[df['name'] == ctype].distance).tolist())

    plt.boxplot(ppm_data, labels=cabtypes, showfliers=fliers, patch_artist=True, boxprops={'facecolor': color})
    plt.title(title)
    plt.xlabel('Cab Type')
    plt.ylabel('Price per Mile (USD/mile)')
    plt.grid()
    plt.show()

    return f