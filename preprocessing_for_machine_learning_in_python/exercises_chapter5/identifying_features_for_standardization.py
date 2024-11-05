# Check the variance of the seconds and minutes columns
print(ufo[['seconds', 'minutes']].var())

# Log normalize the seconds column
ufo["seconds_log"] = np.log(ufo.seconds)

# Print out the variance of just the seconds_log column
print(ufo.seconds_log.var())