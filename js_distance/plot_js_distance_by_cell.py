import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib

muscles = ['bwm_anterior', 'bwm_far_posterior', 'bwm_head_row_1', 'bwm_head_row_2', 'bwm_posterior']

times = [300, 360, 420, 480, 545, 615, 715]

result = pd.DataFrame(index = muscles, columns = times)

colors = ['red', 'blue', 'green', 'pink', 'orange']
color_dict = {}

for i, muscle in enumerate(muscles):
    df = pd.read_csv('js_distance/across_time/' + muscle + '_distance.csv', index_col=0)
    s = df.iloc[0]
    s.drop(s.index.tolist()[0], inplace=True)
    s.index = times[len(s.index)*-1:]

    color_dict[muscle] = colors[i]
    result.loc[muscle] = s

print(result)

result = result.T
lines = result.plot.line(color=color_dict)
plt.title('JSD of cell compared to first time point')
plt.rcParams.update({'font.size': 52})
fig = matplotlib.pyplot.gcf()
# fig.set_size_inches(15, 10)
# plt.show()
plt.savefig('asdf.png', bbox_inches='tight', pad_inches=.25)
