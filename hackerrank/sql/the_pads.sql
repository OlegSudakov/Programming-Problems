// https://www.hackerrank.com/challenges/the-pads

SELECT CONCAT(NAME,
             CASE OCCUPATION
             WHEN "Actor" THEN "(A)"
             WHEN "Doctor" THEN "(D)"
             WHEN "Professor" THEN "(P)"
             WHEN "Singer" THEN "(S)"
             END) AS NAME
FROM OCCUPATIONS
ORDER BY NAME;
SELECT CONCAT("There are total ",OC," ",O,"s.")
FROM (
    SELECT LCASE(OCCUPATION) AS O, COUNT(OCCUPATION) AS OC
    FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY OC ASC, O ASC
) AS T
