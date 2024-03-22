# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv('divorce.csv', parse_dates = ['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])
print(divorce.dtypes)