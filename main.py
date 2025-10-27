import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("student-mat.csv", sep=';')

# Your code starts here

# 1. Compute mean G3 for each studytime category
mean_g3_by_study = df.groupby("studytime")["G3"].mean().reset_index()

# 2. Create a bar chart for studytime
plt.figure(figsize=(8, 5))
sns.barplot(
    x="studytime",
    y="G3",
    data=mean_g3_by_study,
    palette="Blues_d"
)
plt.title("Mean Final Grade (G3) by Study Time Category")
plt.xlabel("Study Time Category")
plt.ylabel("Mean G3")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 3. Identify which studytime has the highest average G3
max_row = mean_g3_by_study.loc[mean_g3_by_study["G3"].idxmax()]
print(f"Studytime category with highest average G3: {int(max_row['studytime'])} "
      f"(mean G3 = {max_row['G3']:.2f})\n")

# 4. Compute and display mean G3 for students with and without internet
mean_g3_by_internet = df.groupby("internet")["G3"].mean().reset_index()
print("Average G3 by Internet Access:")
print(mean_g3_by_internet.to_string(index=False))

# (Optional) Bar chart for internet access
plt.figure(figsize=(6, 4))
sns.barplot(
    x="internet",
    y="G3",
    data=mean_g3_by_internet,
    palette="Pastel1"
)
plt.title("Mean Final Grade (G3) by Internet Access")
plt.xlabel("Internet Access (yes/no)")
plt.ylabel("Mean G3")
plt.tight_layout()
plt.show()

# 5. Compare median G3 for students with absences above and below the dataset median
median_absences = df["absences"].median()
below_median = df[df["absences"] < median_absences]["G3"]
above_median = df[df["absences"] >= median_absences]["G3"]

median_below = below_median.median()
median_above = above_median.median()

print(f"Dataset median absences: {median_absences}")
print(f"Median G3 for absences below median: {median_below}")
print(f"Median G3 for absences at or above median: {median_above}")

# Optionally, perform a t-test to see if the difference is significant
t_stat, p_value = ttest_ind(below_median, above_median, equal_var=False)
print(f"\nT-test comparing G3 medians:")
print(f"  t-statistic = {t_stat:.3f}, p-value = {p_value:.3f}")