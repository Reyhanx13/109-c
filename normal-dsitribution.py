import pandas as pd
import statistics
import csv

df=pd.read_csv("normal-distribution.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

print("mean","median","mode is".format(height_mean,height_mode,height_median))
print("mean","median","mode is".format(weight_mean,weight_median,weight_mode))

height_std_daviration=statistics.stdev(height_list)
weight_std_daviration=statistics.stdev(weight_list)

height_first_std_daviration_start,height_first_std_daviration_end=height_mean-height_std_daviration,height_mean+height_std_daviration
weight_first_std_daviration_start,weight_first_std_daviration_end=weight_mean-weight_std_daviration,weight_mean+weight_std_daviration

print(height_first_std_daviration_start,height_first_std_daviration_end,weight_first_std_daviration_start,weight_first_std_daviration_end)


