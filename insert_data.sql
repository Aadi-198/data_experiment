-- query_clean
INSERT OR IGNORE INTO clean_movies (title, year, rating) VALUES (?, ?, ?);

-- query_quarantine
INSERT OR IGNORE INTO quarantined_movies (title, raw_year, raw_rating) VALUES (?, ?, ?);