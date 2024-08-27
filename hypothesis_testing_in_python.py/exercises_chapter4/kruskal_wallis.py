# Run a Kruskal-Wallis test on weight_kilograms vs. shipment_mode
kw_test = pingouin.kruskal(data = late_shipments,
                           dv = 'weight_kilograms',
                           between = 'shipment_mode')



# Print the results
print(kw_test)