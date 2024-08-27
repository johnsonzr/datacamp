# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results =  pingouin.ttest(sample_dem_data['dem_percent_12'], sample_dem_data['dem_percent_16'], paired = True)




# Print paired t-test results
print(paired_test_results)


# Conduct a Wilcoxon test on dem_percent_12 and dem_percent_16
wilcoxon_test_results = pingouin.wilcoxon(x=sample_dem_data['dem_percent_12'],
                                          y=sample_dem_data['dem_percent_16'],
                                          alternative='two-sided')



# Print Wilcoxon test results
print(wilcoxon_test_results)