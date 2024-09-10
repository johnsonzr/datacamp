# Instantiate a TTestIndPower object
power_analysis = TTestIndPower()

# Conduct a power analysis to determine the required sample size
required_n = power_analysis.solve_power(
    effect_size=.5, 
    alpha=.05, 
    power=.9, 
    ratio=1)

print(required_n)