import matplotlib.pyplot as plt
import pandas as pd
import optimizely
!pip install optimizely-sdk


# Create an Optimizely client object
client = optimizely.Client(api_token="YOUR_API_TOKEN",
                           project_id="YOUR_PROJECT_ID")

# Get the results of the experiment
results = client.experiments.get_results(experiment_id="EXPERIMENT_ID")

# Convert the results data to a pandas DataFrame
df = pd.DataFrame(results)

# Calculate the conversion rate for each variation
df["conversion_rate"] = df["conversions"] / df["visitors"]

# Calculate the average time spent for each variation
df["avg_time_spent"] = df["total_time_spent"] / df["visitors"]

# Print the results
print(df)

# Create a bar chart of the conversion rates
df.plot(kind="bar", x="variation_name", y="conversion_rate")

# Show the plot
plt.show()
