import statistics


mylist = [1, 2, 7, 53, 90, 4, 80, 23, 7]

print(mylist)

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
