# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova(data = late_shipments,
                               dv = 'pack_price',
                               between = 'shipment_mode')



# Print anova_results
print(anova_results)