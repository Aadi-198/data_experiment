#Import modules
import csv
import sqlite3 #Built-in SQL database tool

#Phase:1 Extract Data from the messy file 'movies.csv'

print("\nExtacting Data ...\n")

raw_movies = []

#Open and read the 'messy' data
with open('movies.csv', mode = 'r') as file: #There are different modes - reading, wrinting and appending, r stands for reading
    csv_reader = csv.DictReader(file)
    for row in csv_reader: #Scan every row to append the new file (organised data)
        print(f"Extracted Row : {row}")
        raw_movies.append(row)

print(f"Succesfully extracted {len(raw_movies)} rows.") #Show the number files extracted

#Run the code (if possible use command line tools)
#Don't just run it break it, build it, change it and experiment with it !

#So far we have extracted raw data now we will organise it !

#Phase:2 Transforming the data

print("\nTransforming Data ...\n")

clean_movies = []
quarantine_movies = []

for row in raw_movies:
    movie_name = row['movie_name']
    raw_year = row['release_year']
    raw_rating = row['rating']  # Fixed: Match the exact column name in your CSV
    
    try:
        # Use the variables you extracted above!
        clean_year = int(raw_year.strip())
        
        # Use the raw_rating variable here
        clean_rating = float(raw_rating.strip())
        
        # Handle negative numbers business logic
        if clean_rating < 0:
            print(f"⚠️ Fixing '{movie_name}': Negative rating. Defaulting to 0.0.")
            clean_rating = 0.0  
            
        # Structure the clean data
        clean_movie_data = {
            "name": movie_name,
            "year": clean_year,
            "rating": clean_rating
        }
        clean_movies.append(clean_movie_data)
        print(f"✅ Cleaned: {movie_name}")
        
    except ValueError as e:
        # If the integer or float conversion fails, it lands here safely
        print(f"❌ Quarantined '{movie_name}': Data format mismatch.")
        quarantine_movies.append(row)

# Print the final report out of the loop
print(f"\nTransformation complete!")
print(f"Clean rows ready for database: {len(clean_movies)}")
print(f"Rows isolated in quarantine: {len(quarantine_movies)}\n")

#Run the file again

#Phase:3 Loading the data (Load)

print("\nLoading Data ...\n")

connection = sqlite3.connect('movies.db') #Make a database and connect to it

cursor = connection.cursor() #We need an object to execute SQL commands, just like we need a cursor on our device to control it

#Although we can write SQL in this file, it will be so messy and not a good practise
#So make a new file schema.sql in the same folder

with open('schema.sql', mode='r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL code directly from the file
cursor.executescript(sql_script)
print("✅ Database table initialized using schema.sql.")

# 3. Loop through our clean list and inject the rows into the database
for movie in clean_movies:
    cursor.execute('''
        INSERT INTO clean_movies (title, year, rating)
        VALUES (?, ?, ?)
    ''', (movie['name'], movie['year'], movie['rating']))
    print(f"Loaded into DB: {movie['name']}")

# 4. Commit changes and close the connection
connection.commit()
connection.close()

print("\n🎉 PIPELINE COMPLETE: Clean data locked in 'movies.db' using decoupled SQL!\n")

#Fun Fact : The clear command comes in clutch if your terminal looks like a battle field