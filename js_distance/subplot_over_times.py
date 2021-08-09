import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.lines import Line2D

custom_lines = [] 

bins = ['270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']
muscles = ['bwm_anterior', 'bwm_far_posterior', 'bwm_head_row_1', 'bwm_head_row_2', 'bwm_posterior']
colors = ['red', 'blue', 'green', 'k', 'm']

times = [300, 360, 420, 480, 545, 615, 715]

result_dict = {}
color_dict = {}

for i in range(len(muscles)):
   custom_lines.append(Line2D([0], [0], color=colors[i], lw=2))

for index, muscle in enumerate(muscles):
    result_dict[muscle] = pd.DataFrame(index = muscles, columns = bins)
    color_dict[muscle] = colors[index]

for bin in bins:
    df = pd.read_csv('js_distance/across_cells/' + bin + '_distance.csv', index_col=0)
    for index, row in df.iterrows():
        for i, v in row.iteritems():
            if not math.isnan(v):
                result_dict[index].at[i, bin] = v
                result_dict[i].at[index, bin] = v


fig, axes = plt.subplots(nrows=3, ncols=2)


x = True

plt.suptitle('JSD between cells')
for i, muscle in enumerate(muscles):
    result_dict[muscle].columns = times
    result_dict[muscle].drop(muscle, inplace=True)
    result_dict[muscle] = result_dict[muscle].T
    result_dict[muscle].plot.line(color=color_dict,ax=axes[i//2, i%2], legend=None, title=muscle)
    

fig.tight_layout()
fig.delaxes(axes[2,1])
ax = plt.gca()
ax.legend().set_visible(True)
ax.legend(custom_lines, muscles, bbox_to_anchor = (1.3, 1.2))


plt.savefig('js_distance/across_cells/across_cell_subplot.png')