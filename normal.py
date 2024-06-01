import pandas as pd
import statistics
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv("StudentsPerformance.csv")

# Assuming you want to analyze 'math score'
scores = data["math score"]

# Calculate mean, median, mode, and standard deviation
mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)
std_dev = statistics.stdev(scores)

# Find the starting and ending points of standard deviation
start_point = mean - std_dev
end_point = mean + std_dev

# Get the data points between the standard deviation
within_std_dev = [score for score in scores if start_point < score < end_point]

# Find the percentage of data within the standard deviation
percentage_within_std_dev = (len(within_std_dev) / len(scores)) * 100

# Plotting histogram
plt.figure(figsize=(10, 6))
plt.hist(scores, bins=20, color='skyblue', edgecolor='black')
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label='Mean')
plt.axvline(median, color='green', linestyle='dashed', linewidth=1, label='Median')
plt.axvline(mode, color='orange', linestyle='dashed', linewidth=1, label='Mode')
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.title('Histogram of Math Scores')
plt.legend()
plt.grid(True)
plt.show()

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std_dev)
print("Starting Point of Standard Deviation:", start_point)
print("Ending Point of Standard Deviation:", end_point)
print("Data Points within Standard Deviation:", within_std_dev)
print("Percentage of Data within Standard Deviation:", percentage_within_std_dev)




