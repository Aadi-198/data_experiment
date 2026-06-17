#Import modules
import csv

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