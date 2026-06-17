/*
SQL is not case-sensitive
But often the community writes SQL commands in CAPS
It is done to easily distinguish between SQL commands and local variables and data
It is easier to skim-read it since you will skip the data and focus on the SQL command in caps
*/

CREATE TABLE IF NOT EXISTS clean_movies( -- this make a table if it doesn't exist
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    year INTEGER,
    rating REAL
);

/* 
So, far we have made the table where we will insert our clean data
But we aren't sure if we can't see it
To see the database, I recommend installing TablePlus
Now try connecting to movies.db in TablePlus
If you see a sqlite_sequence table, don't worry about that, it was auto create and is IMPORTANT
*/