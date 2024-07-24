# Update prediction data with odds_ratio
prediction_data["odds_ratio"] = prediction_data.has_churned / (1 - prediction_data.has_churned)

# Print the head
print(prediction_data.head())