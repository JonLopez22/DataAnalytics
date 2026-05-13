import statistics

# Sample dataset
data = [10, 20, 20, 40, 50]

print("=== Python Statistics Module Demo ===\n")

# mean() average value
print("mean:", statistics.mean(data))

# median() middle value
print("median:", statistics.median(data))

# mode() most common value
print("mode:", statistics.mode(data))

# stdev() standard deviation 
print("stdev:", statistics.stdev(data))

# variance() variance
print("variance:", statistics.variance(data))