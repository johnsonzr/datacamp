# Import the re module
import re

# Write the regex
regex = "@robot\d\W"

# Find all matches of regex
print(re.findall("@robot\d\W", sentiment_analysis))