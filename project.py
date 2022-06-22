import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")
data =  df["reading_time"].tolist()

p_mean = st.mean(data)
p_std = st.stdev(data)
print(f"The population mean:{p_mean}")
print(f"The population std: {p_std}")

fig = ff.create_distplot([data], ["Reading Time"], show_hist = False)
#fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):  
        random_index = random.randint(0, len(data)-1) #5
        value = data[random_index] #data[5]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

    def setup():
    meanlist= []
    for i in range(0, 1000):
        f = random_set_of_mean(100)
        meanlist.append(f)
    mean = st.mean(meanlist)
    std = st.stdev(meanlist)
    print(f"sample mean:{mean}")
    print(f"sample std:{std}")

    fig = ff.create_distplot( [meanlist], ["Sample data"], show_hist = False)
    fig.show()

    setup()