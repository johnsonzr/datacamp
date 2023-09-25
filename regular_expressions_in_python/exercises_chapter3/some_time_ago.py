# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\s\S+\s\S+", date))
# find 27 minutes ago or 4 hours ago

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w\w\s\w+\s\d{4}", date))
# find 23rd june 2018

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w{2}\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))
# find 1st september 2019 17:25