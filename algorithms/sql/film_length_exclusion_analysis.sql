"""
SQL Query: Film Length Exclusion by Rating Statistics
Overview:
    This script retrieves 'film_id', 'title', and 'length' from the DVD rental 
    database, excluding any films with a length falling between the minimum 
    duration of 'R' rated films and the discrete median duration of 'PG-13' 
    rated films. The final output strictly contains films that are either 
    shorter than the R-rated minimum or longer than the PG-13 median.
Technical Implementation:
    - Uses 'PERCENTILE_DISC(0.5)' for a discrete median calculation 
      on integer values.
    - Implements nested scalar subqueries within a 'NOT BETWEEN' clause.
"""
SELECT film_id,
  title,
  length
from film
WHERE length NOT BETWEEN (SELECT MIN (length) FROM film WHERE rating = 'R')
  AND (SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY length)
                FROM film WHERE rating = 'PG-13' )
ORDER BY length ASC, title ASC, film_id ASC
