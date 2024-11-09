import csv

# Read the data from the text file "descriptions.txt"
txt_filename = "descriptions.txt"
parsed_data = {}

# Open and read the text file
with open(txt_filename, mode='r') as file:
    for line in file:
        line = line.strip()  # Remove any leading/trailing whitespace
        if ":" in line:  # Only process lines with a colon (key-value format)
            key, value = line.split(":", 1)  # Split at the first colon
            parsed_data[key.strip()] = value.strip()  # Store key-value pair

# Save parsed data to CSV
csv_filename = "descriptions.csv"

# Open the CSV file for writing
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row (Field Name and Description)
    writer.writerow(["Field Name", "Description"])

    # Write each key-value pair as a row
    for key, value in parsed_data.items():
        writer.writerow([key, value])

print(f"Data has been read from {txt_filename} and saved to {csv_filename}")
