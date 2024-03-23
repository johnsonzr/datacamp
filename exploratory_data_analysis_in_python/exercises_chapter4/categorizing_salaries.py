# Create salary labels
salary_labels = ['entry', 'mid', 'senior', 'exec']

# Create the salary ranges list
salary_ranges = [0, twenty_fifth, salaries_median, seventy_fifth, salaries["Salary_USD"].max()]

# Create salary_level
salaries["salary_level"] = pd.cut(salaries["Salary_USD"],
                                  bins=salary_ranges,
                                  labels=salary_labels)

# For fun
print(salaries.groupby('salary_level')['Salary_USD'].agg(['mean', 'min', 'max']))