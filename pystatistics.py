import statistics
from scipy import stats
import pprint
import pandas as pd


pp=pprint.PrettyPrinter(indent=4).pprint

mylist = [1, 2, 7, 53, 90, 4, 80, 23, 7]

pp(mylist)
print("*"*80)
print(" "*20, "Estimates of location")
print("*"*80)
print("===========statistics============")
print(f"mean:{statistics.mean(mylist)}")
print(f"fmean:{statistics.fmean(mylist)}")
print(f"median:{statistics.median(mylist)}")
print(f"mode:{statistics.mode(mylist)}")
print(f"variance:{statistics.variance(mylist)}")
print(f"pvariance:{statistics.pvariance(mylist)}")
print(f"stdev:{statistics.stdev(mylist)}")
print(f"pstdev:{statistics.pstdev(mylist)}")
print(f"fsum:{statistics.fsum(mylist)}")
print(f"geometric_mean:{statistics.geometric_mean(mylist)}")
print(f"median_high:{statistics.median_high(mylist)}")
print(f"median_low:{statistics.median_low(mylist)}")
print(f"hypop(ecludian distance from origin:{statistics.hypot(*mylist)}")
print("===========scipy stats============")
tm = stats.trim_mean(mylist, 0.2)
print(f"stats.trim_mean:{tm}")
print("*"*80)
print(" "*20, "Estimates of variability")
print("*"*80)
print("===========pandas============")
series = pd.Series(mylist)
print(f"mean abs deviation(l1 norm, manhattan norm):{series.mad()}")
print(f"variance, RMS, l2norm :{series.var()}")
ax = series.plot.box(grid=True)
ax.get_figure().savefig('box.png')
