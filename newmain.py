import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def line_chart_example(x_ser,y_ser):
    plt.plot(x_ser,y_ser,
             label="Population",
             c="green",
             lw="5")
    plt.plot(x_ser,y_ser * 2,
             label="Population *2",
             c="purple",
             lw="--")
    plt.legend()
    plt.ylabel("Polupation (in million)")
    pie.xlabel("City Class")
    plt.title("Chinese")
    lt.savefig("line.png")
    plt.show()

def scatter_chart_example(x_ser,y_ser):
    plt.figure()
    plt.bar(x_ser,y_ser)
    plt.savefig("scatter.png")

def bar_chart_example(x_ser,y_ser):
    plt.figure()
    plt.bar(x_ser,y_ser)
    plt.savefig("bar.png")

def pie_chart_example(values_ser,labels_ser):
    plt.figure()
    plt.pie(values_ser
            lables=lables_ser,
            autopct="%1.1f%%")
    plt.savefig("pie.png")

def histogram_chart_example(values_ser1):
    plt.figure()
    plt.pie(values_ser1)
    plt.savefig("histogram.png")

df = pd.read_csv("merged.csv")
print(df)

group_by_class = df.groupby("Class")
class_pop_ser = grouped_by_class["Population"].sum()
print(class_pop_ser)


line_chart_example(class_pop_ser.index,
                 class_pop_ser)

scatter_chart_example(class_pop_ser.index,
                 class_pop_ser)

bar_chart_example(class_pop_ser.index,
                 class_pop_ser)

pie_chart_example(class_pop_ser.index,
                 class_pop_ser)




mean = 100
stdev = 25
num_datapoints = 1000
rand_data1 = np.random.normal(mean,
                              stdev,
                              num_datapoints)

histogram_chart_example(rand_data1)
