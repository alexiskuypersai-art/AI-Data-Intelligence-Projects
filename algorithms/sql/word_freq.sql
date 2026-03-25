/* Top 10 Meaningful Words Extraction
  ----------------------------------
  1. Tokenize (lower, regex [^a-z0-9''/_-]+)
  2. Filter (length >= 3, exclude stopwords)
  3. Aggregate (count, sort by freq DESC, word ASC)
  Example : 
    word    | freq |
    +---------+------+
    | review  | 5    |
    | build   | 3    |
    | slow    | 3    |
*/
WITH word_extraction AS (
    SELECT 
  regexp_split_to_table(lower(msg), '[^a-z0-9''/_-]+') AS word
    FROM retro_comments
),

cleaned_words AS (
    SELECT w.word
    FROM word_extraction w
    LEFT JOIN stopwords s ON w.word = s.word
    WHERE length(w.word) >= 3  
      AND s.word IS NULL             
)
SELECT 
    word, 
    COUNT(*) AS freq
FROM cleaned_words
GROUP BY word
ORDER BY freq DESC, word ASC
LIMIT 10;
