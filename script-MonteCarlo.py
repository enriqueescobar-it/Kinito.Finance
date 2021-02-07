import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from numpy.core._multiarray_umath import ndarray

style.use('ggplot')

start = dt.datetime(year=2020, month=1, day=1)
end = dt.datetime(year=2020, month=12, day=1)

prices = web.DataReader('AAPL', data_source='yahoo', start='2020-01-01', end='2020-12-01')['Adj Close']
returns = prices.pct_change()

last_price = prices[-1]

# Number of Simulations
num_simulations = 1000
num_days = 252

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()

    price_series = []

    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df[x] = price_series

fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: AAPL')
plt.plot(simulation_df)
plt.axhline(y=last_price, color='r', linestyle='-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()
##### RADAR PLOT #####
import matplotlib.pyplot as plt
import numpy as np

labels = ['Siege', 'Initiation', 'Crowd_control', 'Wave_clear', 'Objective_damage']
int_markers = [0, 1, 2, 3, 4, 5]
str_markers = ["0", "1", "2", "3", "4", "5"]


def make_radar_chart(name, stats_array, attribute_labels=labels, plot_markers=int_markers, plot_str_markers=str_markers):
    label_array: ndarray = np.array(attribute_labels)
    angle_array: ndarray = np.linspace(0, 2 * np.pi, len(label_array), endpoint=False)
    stats_array = np.concatenate((stats_array, [stats_array[0]]))
    angle_array = np.concatenate((angle_array, [angle_array[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angle_array, stats_array, 'o-', linewidth=2)
    ax.fill(angle_array, stats_array, alpha=0.25)
    #ax.set_thetagrids(angle_array * 180 / np.pi, labels)
    plt.yticks(int_markers)
    ax.set_title(name)
    ax.grid(True)
    gridlines = ax.yaxis.get_gridlines()
    for gl in gridlines:
        gl.get_path()._interpolation_steps = 5
    #fig.savefig("static/images/%s.png" % name)
    return plt.show()


make_radar_chart("Agni", [2, 3, 4, 4, 5])  # example
