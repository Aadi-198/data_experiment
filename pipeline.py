import csv

print("\nExtacting Data ...\n")

raw_movies = []

#Open and read the 'messy' data
with open('movies.csv', mode = 'r') as file: #There are different modes - reading, wrinting and appending, r stands for reading
    csv_reader = csv.DictReader(file)
    for row in csv_reader: #Scan every row and append the new file (organised data)
        print(f"Extracted Row : {row}")
        raw_movies.append(row)

print(f"Succesfully extracted {len(raw_movies)} rows.") #Show the number files extracted