# compute single mean t-test
import numpy as np
from scipy import stats

# Sample data for each demo group
demo_group1 = np.array([1, 2, 3, 4, 5])
demo_group2 = np.array([2, 4, 6, 8, 10])
# Add more demo groups if needed

# Expected value for comparison
expected_value = 3.5

# Perform t-test for each demo group
demo_groups = [demo_group1, demo_group2]  # Add more demo groups if needed
for i, group in enumerate(demo_groups):
    t_statistic, p_value = stats.ttest_1samp(group, expected_value)
    print(f"Demo Group {i+1}: t-statistic = {t_statistic}, p-value = {p_value}")