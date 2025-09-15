import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import  matplotlib
from IPython.core.pylabtools import figsize
from matplotlib.lines import lineStyles
from mercurial.obsutil import marker

matplotlib.use('TkAgg')

############################
# 1. Line Plot -> plt.plot()
############################

# Purpose: Show trends (time-series, loss curves, trends)
# Syntax: plt.plot(x, y, color=..., linestyle=..., marker=..., label=...)

'''
Arguments to know:

color ("blue", "r", "#FF5733")
linestyle ("-", "--", "-.", ":")
marker ("o", "s", "x", ".")
label → for legend
'''

#  Example :-

# x = np.arange(1,11)
# y = x ** 2
#
# plt.plot(x,y, color="blue", linestyle="--",  label="y = x^2", marker="o")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Line plot Example")
# plt.legend()
#
# plt.show()

#########################
# 2. Scatter Plot -> plt
#########################

# Purpose: visualize features, clusters, correlations
# Syntax: plt.scatter(x, y, color=..., s=..., alpha=..., label=...)

'''
Useful args:

color / c → color of points
s → size of points
alpha → transparency (0 = invisible, 1 = solid)
label → name for legend
'''

# Example :-

x = np.random.rand(50)
y = np.random.rand(50)
#
# plt.scatter(x,y, color="red", s=60 , alpha=0.6, label="Points")
# plt.title("scatter plot example")
# plt.legend()
# plt.show()

############################
# 3. Histogram -> plt.hist()
############################

# Purpose:  Check distribution of a feature (e.g. age, income)
# Syntax: plt.hist(data, bins=..., color=..., alpha=..., edgecolor=...)

'''
Useful args:

bins → number of groups/divisions
color → bar color
alpha → transparency
edgecolor → outline color of bars
'''

# Example :-

data = np.random.randn(1000)
#
# plt.hist(data, bins=30, color="purple", alpha=0.7, edgecolor="black")
# plt.title("Histogram Example")
# plt.show()


###########################
# 4. Bar Chart -> plt.bar()
###########################

# Purpose: Compare categories (e.g. accuracy of different models)
# Syntax: plt.bar(categories, values, color=..., width=..., alpha=..., label=...)

'''
Useful args:

color → bar color
width → bar width (default = 0.8)
alpha → transparency
label → for legend
'''

# Example :-

# ai_models = ["chatgpt","deepseek","qwen","claude"]
# points = [95,85,90,70]
#
# plt.bar(ai_models, points, color="green", alpha=0.7)
# plt.title("AI Models Comparison")
# plt.ylabel("Accuracy")
# plt.show()

########################################################
# 5. Multi-Plots in One Figure -> subplot() / subplots()
########################################################

# Purpose: Compare multiple graphs side by side.

# Example :-

# fig, axs = plt.subplots(1,2, figsize=(10,4))
#
# # Line
# axs[0].plot(x,y, color="blue")
# axs[0].set_title("Line plot")
#
# # Histogram
# axs[1].hist(data, bins=20, color="orange")
# axs[1].set_title("Histogram")
#
# plt.tight_layout()
# plt.show()

#################################################
# 6. Integration with Pandas (super common in ML)
#################################################

df = pd.DataFrame({
    "Height": np.random.normal(170,10,100),
    "Weight": np.random.normal(65,15,100)
})

df.plot(kind="scatter", x="Height", y="Weight", alpha=0.5, color="red")
plt.title("Height v/s Weight")
plt.show()

'''
👆 here df.plot() is Pandas own plot() method which is nothing but a wrapper around plyplot's plot() method

So;
plt.plot() = raw Matplotlib function.
df.plot() = Pandas helper method that uses Matplotlib under the hood.

** so, Why does Pandas have its own .plot()?

Because most of the time in ML we'll work with DataFrames (after cleaning data).
Instead of extracting columns manually and passing them into plt, we can directly plot from the DataFrame.

** ⚡ So the rule is:

If we’re working with raw arrays (NumPy) → use plt.plot, plt.scatter, etc.
If ywe’re working with Pandas DataFrame → use df.plot(...).
'''

'''
🔧 Helper Functions to Use All the Time

plt.title("...")

plt.xlabel("...")

plt.ylabel("...")

plt.legend()

plt.grid(True)

plt.xlim(min, max) / plt.ylim(min, max)

plt.show() (always ends the plot)
'''

'''
📊 Multi-Plot Layouts

plt.subplot(rows, cols, index) → quick grids

fig, ax = plt.subplots() → preferred way in ML notebooks
'''