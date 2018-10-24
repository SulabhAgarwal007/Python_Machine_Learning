import matplotlib.pyplot as plt;
import numpy as np;

height = np.round(np.random.normal(1.5, 0.2, 10), 2)
weight = np.round(np.random.normal(2.5, 0.2, 10), 2)

plt.plot(height, weight)
plt.show()
plt.clf()

plt.scatter(height, weight)
plt.show()
plt.clf()

plt.hist(height, bins=15)
plt.show()
plt.clf()

# plt.xlabel(), plt.ylabel(), plt.title(), plt.xscale, plt.yticks

# ~~~~~~~~~~~
# Scatter plot

# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()
#~~~~~~~~~~