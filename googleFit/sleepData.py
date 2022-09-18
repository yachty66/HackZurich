import pandas as pd


def getSleepData():
    #tausche jedes , mit einem .
    with open('sleepData.csv', 'r') as f:
        for line in f:
            line = line.replace(",", ".")
        
    #tausche jedes ; mit einem ,
    with open("sleepData.csv", "r") as f:
        for line in f:
            line = line.replace(";", ",")

    #drop every column except 2 and 4 
    pd.read_csv('sleepData.csv', sep=',', usecols=[2,4])




if __name__ == "__main__":
    getSleepData()
