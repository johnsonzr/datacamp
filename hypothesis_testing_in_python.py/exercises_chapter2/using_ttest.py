# Conduct a t-test on diff
test_results = pingouin.ttest(x = sample_dem_data['diff'],
                              y = 0,
                              paired = True,
                              alternative = 'two-sided')




# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x = sample_dem_data['dem_percent_12'],
                                     y = sample_dem_data['dem_percent_16'],
                                     paired = True,
                                     alternative = 'two-sided')



                              
# Print the paired test results
print(paired_test_results)