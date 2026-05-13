# requirement 1
import statistics

# requirement 2
analyst = input("Enter analyst name: ")
region = input("Enter region: ")

# requirement 3
print("Enter daily sales for 7 days (one per line):")
sales = [float(input(f" Day {i+1}: $")) for i in range(7)]

# requirement 4
def analyze_sales(analyst, region, sales):
    return mean, median, mode, stdev, total, high, low

# requirement 5
def analyze_sales(analyst, region, sales):
    mean = statistics.mean(sales)
    median = statistics.median(sales)
    mode = statistics.mode(sales)
    stdev = statistics.stdev(sales)
    total = sum(sales)
    high = max(sales)
    low = min(sales)
    return mean, median, mode, stdev, total, high, low

# requirement 6
mean, median, mode, stdev, total, high, low = analyze_sales(analyst, region, sales)
print(f"""
======= Weekly Sales Statistics Report =======
Analyst : {analyst}
Region : {region}
Data : {sales}
------------------------------------------------
Total Revenue : ${total:.2f}
Mean (avg) : ${mean:.2f}
Median : ${median:.2f}
Mode : ${mode:.2f}
Std Deviation : ${stdev:.2f}
Highest Day : ${high:.2f}
Lowest Day : ${low:.2f}
=================================================
""")