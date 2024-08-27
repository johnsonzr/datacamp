# Perform a goodness of fit test on the incoterm counts n
gof_test = chisquare(f_obs = incoterm_counts['n'], f_exp= hypothesized['n'])


# Print gof_test results
print(gof_test)