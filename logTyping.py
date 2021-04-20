import os
import pathlib
import random
import pandas as pd
from datetime import datetime
import sys

 
def updateTypingPerformance(df,datedPerformance):
    if "Unnamed: 0" in df.columns:
        df.drop("Unnamed: 0", axis=1, inplace=True)
    df.loc[len(df)] = datedPerformance
    return df


def typePractice(typingDataset):
    files = list(typingDataset.iterdir())
    file = random.choice(files)
    f = open(file, "r")
    numberOfLines = len(f.readlines())
    print(file)
    print(numberOfLines)
    if numberOfLines>10:
        numberOfLines=10

    os.system(f"mlt file  --n-lines {numberOfLines} {file}")


typingDatasetFolder = "/home/lucassoares/Desktop/projects/self_track/data/typingDataset"
typingDataset = pathlib.Path(typingDatasetFolder)
typingPerformance = "/home/lucassoares/Desktop/projects/self_track/data/typingPerformance.csv"
df = pd.read_csv(typingPerformance)
typePractice(typingDataset)

performance = []

date = str(datetime.now())

wpm = input("What was the wpm?")
acc = input("Waht was the accuracy?")
cont = input("Continue typing?")
performance.append(date)
performance.append(wpm)
performance.append(acc)

updateTypingPerformance(df,performance)
while cont=="y":
    performance = []
    typePractice(typingDataset)
    date = str(datetime.now())
    wpm = input("What was the wpm?")

    acc = input("Waht was the accuracy?")

    performance.append(date)
    performance.append(wpm)
    performance.append(acc)

    updateTypingPerformance(df,performance)
    
    cont = input("Continue typing?")


if len(sys.argv)>1:
    if sys.argv[1]=="plot":
        df["wpm"].plot()
        plt.show()

df.to_csv("/home/lucassoares/Desktop/projects/self_track/data/typingPerformance.csv", index=False)
    








