import csv
#pip install -r requirements.txt
# View -> Terminal
#cd to location of project where requirements text is located then use command.
#Export CSV files without Headers from sql to import them below!!
## Make sure you have Python and pip installed and added to your system's PATH environment variable##
local_table_file = r"C:\"
server_table_file = r"C:\"
differences_file = r"C:\"

# Read the structures of the local table
with open(local_table_file, 'r', encoding='utf-8-sig') as local_file:
    local_reader = csv.reader(local_file)
    local_table = {row[0]: row[1] for row in local_reader}

# Read the structures of the server table
with open(server_table_file, 'r', encoding='utf-8-sig') as server_file:
    server_reader = csv.reader(server_file)
    server_table = {row[0]: row[1] for row in server_reader}

# Find the differences between the tables
differences = {}

# Find the differences in the local table
for table, local_value in local_table.items():
    server_value = server_table.get(table)
    if server_value is None:
        differences[table] = {'Local': local_value, 'Server': 'Not Found'}
    elif local_value != server_value:
        differences[table] = {'Local': local_value, 'Server': server_value}

# Find the differences in the server table
for table, server_value in server_table.items():
    if table not in local_table:
        differences[table] = {'Local': 'Not Found', 'Server': server_value}

# Export the differences to a new CSV file
with open(differences_file, 'w', newline='', encoding='utf-8-sig') as diff_file:
    diff_writer = csv.writer(diff_file)
    diff_writer.writerow(['Table', 'Local', 'Server'])

    for table, values in differences.items():
        diff_writer.writerow([table, values['Local'], values['Server']])

print(f"Table differences exported to {differences_file}")