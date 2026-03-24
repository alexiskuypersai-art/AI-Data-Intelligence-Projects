/* 
INSTRUCTION: Extract users and their comma-separated pet names starting with 'M' from a JSONB array.
CONCEPTS: 
  1. JSON Unnesting (jsonb_array_elements)
  2. Text Extraction (->>)
  3. String Aggregation (STRING_AGG)
EXAMPLE: 
  id  | user_name       | pet_names        |
------+-----------------|------------------|
  15  | Kelley Ebert    | Moriah           |
  16  | Hayley Schiller | Micheal, Magaret |
*/

SELECT 
    id,
    info ->> 'name' AS user_name,
    STRING_AGG(pet_data ->> 'name', ', ') AS pet_names 
FROM 
    users,
    jsonb_array_elements(info -> 'pets') AS pet_data
WHERE 
    pet_data ->> 'name' ILIKE 'M%'
GROUP BY 
    id, 
    info ->> 'name';
