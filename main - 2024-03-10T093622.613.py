import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
bat_calls_data = pd.read_csv('bat_calls_dataset.csv')

# Display basic statistics of the dataset
print("Basic statistics of the bat echolocation calls dataset:")
print(bat_calls_data.describe())

# Perform hypothesis testing to compare mean call duration between two species
species_A_calls = bat_calls_data[bat_calls_data['Species'] == 'Species A']['Call Duration (ms)']
species_B_calls = bat_calls_data[bat_calls_data['Species'] == 'Species B']['Call Duration (ms)']

t_stat, p_value = stats.ttest_ind(species_A_calls, species_B_calls, equal_var=False)
print("\nHypothesis Testing Results:")
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Visualize the distribution of call durations by species
plt.figure(figsize=(8, 6))
sns.histplot(data=bat_calls_data, x='Call Duration (ms)', hue='Species', bins=20, kde=True, palette='muted')
plt.title('Distribution of Bat Echolocation Call Durations by Species')
plt.xlabel('Call Duration (ms)')
plt.ylabel('Frequency')
plt.legend(title='Species')
plt.grid(True)
plt.show()

