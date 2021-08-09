import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib

bins = ['270_330', '330_390', '390_450', '450_510', '510_580', '580_650', 'gt_650']
muscles = ['bwm_anterior', 'bwm_far_posterior', 'bwm_head_row_1', 'bwm_head_row_2', 'bwm_posterior']

times = [300, 360, 420, 480, 545, 615, 715]

result_dict = {}
color_dict = {}


colors = ['red', 'blue', 'green', 'pink', 'orange']

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

for muscle in muscles:
    result_dict[muscle].columns = times
    result_dict[muscle].drop(muscle, inplace=True)
    result_dict[muscle] = result_dict[muscle].T
    lines = result_dict[muscle].plot.line(color=color_dict)
    print(result_dict[muscle])
    plt.title(muscle + ' JSD')
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(15, 10)
    # plt.show()
    plt.savefig('js_distance/plots/' + muscle + '_plot.png', bbox_inches='tight', pad_inches=.25)