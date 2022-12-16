import csv

# Open csv file
data = open('resources/example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
for line in data_lines:
    print(line)

# pull data out of csv file
all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])

full_name = []
for line in data_lines[1:]:
    full_name.append(line[1] + ' ' + line[2])

# Create a file and store date
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['1', '2', '3'])
csv_writer.writerows([['1', '2', '3'], ['1', '2', '3']])
file_to_output.close()

# Add a line
f = open('to_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1', '2', '3'])
file_to_output.close()
