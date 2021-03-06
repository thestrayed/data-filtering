import csv

# Constant variable
READ_PATH = './raw_dataset/DL022016.csv'
WRITE_PATH = './filtered_dataset/DL022016.csv'

# Rule for filtering data
ROW_NO = 23
RULES = [''] * ROW_NO
RULES[2] = '05/02/2016' # date something
RULES[10] = 'CBG' # company name CBG

# Initialize data
filtered_data = []

# Read data from file
with open(READ_PATH, newline='\n') as read_csvfile:
    reader = csv.reader(read_csvfile, delimiter=',')
    # Skip header line
    next(reader, None)
    for row in reader:
        temp_filtered_data = []
        status = True
        # Iterate row and rules together in parallel manner
        for raw_data, rule in zip(row, RULES):
            if rule != '':
                if raw_data.lower() != rule.lower():
                    status = False

        if status:
            filtered_data.append(row)
        
# if filtered_data is not empty write file
if filtered_data:
    with open(WRITE_PATH, 'w', newline='\n') as write_csvfile:
        writer = csv.writer(write_csvfile, delimiter=',')
        # Write default header for filtered_data file
        writer.writerow(['VAR1', 'VAR2', 'VAR3', 'VAR4', 'VAR5', 'VAR6', 'VAR7', 'VAR8', 'VAR9', 'VAR10', 'VAR11',
            'VAR12', 'VAR13', 'VAR14', 'VAR15', 'VAR16', 'VAR17', 'VAR18', 'VAR19', 'VAR20', 'VAR21', 'VAR23', 'VAR24'])
        # Write filter_data to file
        for f in filtered_data:
            writer.writerow(f)
