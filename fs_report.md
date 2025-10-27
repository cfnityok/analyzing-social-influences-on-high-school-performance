This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or first three lines for files with .csv extensions

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- This file includes only .ipynb and .csv file contents in full or partial form
- All other file types are represented only through the directory structure
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files

# Directory Structure

````
./
fs_report.md
main.py
student-mat.csv
````

# Files

## File: student-mat.csv
````
school;sex;age;address;famsize;Pstatus;Medu;Fedu;Mjob;Fjob;reason;guardian;traveltime;studytime;failures;schoolsup;famsup;paid;activities;nursery;higher;internet;romantic;famrel;freetime;goout;Dalc;Walc;health;absences;G1;G2;G3
"GP";"F";18;"U";"GT3";"A";4;4;"at_home";"teacher";"course";"mother";2;2;0;"yes";"no";"no";"no";"yes";"yes";"no";"no";4;3;4;1;1;3;6;"5";"6";6
"GP";"F";17;"U";"GT3";"T";1;1;"at_home";"other";"course";"father";1;2;0;"no";"yes";"no";"no";"no";"yes";"yes";"no";5;3;3;1;1;3;4;"5";"5";6
````

## File: main.py
````
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
plt.show()````
