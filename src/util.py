import numpy as np
import matplotlib.pyplot as plt

def print_line(len=100, character="-"):
    print(character * len)

def plot_returns(returns_df):
    ax = returns_df.plot.bar(color=np.where(returns_df > 0, "g", "r"))
    ax.set_xticks([])
    plt.title("Returns")
    plt.xlabel("Time")
    plt.ylabel("Returns")
    plt.show()
