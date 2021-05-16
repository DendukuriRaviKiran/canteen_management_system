import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import sys
import sqlite3

def viewg(g1):
    

    for row in g1.values():
        pass

    height=[]
    bars = ()
    bars= tuple(g1.keys())



    print(type(g1.values()))
    height= list(g1.values())
    print(bars, height)
    
    y_pos = np.arange(len(bars))
    plt.bar(bars,height, color=['blue', 'cyan', 'orange', 'red', 'pink'])
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Graph')
    plt.show()

if __name__ == "__main__":
    d={'jan':2,'feb':23}
    viewg(d)



