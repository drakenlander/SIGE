import numpy as np
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
import careers

length = len(careers.lenRes)

x = careers.legendArr
subX = ["> " + str(careers.year), "< " + str(careers.year)] * length
y = careers.lenRes

figsize = (2.25 * length, 5)
radius = 1
width = 0.5
size = 0.2

cmap = plt.colormaps["tab20"]
bar_colors_legend = [Line2D([0], [0], color=cmap(0), lw=4),
                     Line2D([0], [0], color=cmap(2), lw=4)]
outer_colors = [0] * length
outer_colors_iter = 0
inner_colors = [0] * (length * 2)
inner_colors_iter = 0
inner_colors_legend = [Line2D([0], [0], color=cmap(14), lw=4),
                       Line2D([0], [0], color=cmap(15), lw=4)]

for i in range(length):
    outer_colors[i] = outer_colors_iter
    outer_colors_iter += 2

for j in range(length * 2):
    inner_colors[j] = inner_colors_iter
    inner_colors_iter += 1

outer_colors = cmap(outer_colors)
inner_colors = cmap(inner_colors)


# Bar Chart
def barChart():
    plt.figure(figsize=figsize)

    plt.bar(x, y, color=cmap(0), width=width)
    # plt.ylim(0, len(careers.resLim))

    plt.xlabel("Carreras Universitarias")
    plt.ylabel("Graduados por Carrera Universitaria")
    plt.tight_layout()

    plt.show()


# Stacked Bar Chart
def stackedBarChart():
    fig, ax = plt.subplots(figsize=figsize)
    bottom = np.zeros(length)
    barV = np.zeros((2, length))

    for e in range(length):
        barV[0][e] = careers.lenYearRes[e]
        barV[1][e] = careers.yearDiffRes[e]

    for bar in barV:
        ax.bar(x, bar, width=width, bottom=bottom)
        bottom += bar

    plt.xlabel("Carreras Universitarias")
    plt.ylabel("Graduados por Carrera Universitaria")
    plt.legend(bar_colors_legend, subX, title="Distribución de Tiempo",
               bbox_to_anchor=(1.0, 1.0), loc="center")
    plt.tight_layout()

    plt.show()


# Pie Chart
def pieChart():
    plt.figure(figsize=figsize)

    plt.pie(y, colors=outer_colors, wedgeprops=dict(edgecolor='w'), labels=x, autopct='%1.1f%%')

    '''
    plt.legend(x, title="Distribución de Graduados",
               bbox_to_anchor=(0.0, 1.0), loc="center")
    '''
    plt.tight_layout()

    plt.show()


# Nested Pie Chart
def nestedPieChart():
    fig, ax = plt.subplots(figsize=figsize)

    pieV = np.zeros((length, 2))

    for e in range(length):
        pieV[e][0] = careers.lenYearRes[e]
        pieV[e][1] = careers.yearDiffRes[e]

    ax.pie(pieV.sum(axis=1), radius=radius, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'), labels=x)
    ax.pie(pieV.flatten(), radius=radius - size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'),
           autopct='%1.1f%%')

    '''
    careerLegend = plt.legend(x, title="Distribución de Graduados",
                              bbox_to_anchor=(0.0, 0.0), loc="center")
    ax.add_artist(careerLegend)
    '''
    ax.legend(inner_colors_legend, subX, title="Distribución de Tiempo",
              bbox_to_anchor=(1.0, 1.0), loc="center")
    plt.tight_layout()

    plt.show()
