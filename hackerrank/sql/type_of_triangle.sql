// https://www.hackerrank.com/challenges/what-type-of-triangle

SELECT CASE
    WHEN A+B <= C THEN "Not A Triangle"
    WHEN A+C <= B THEN "Not A Triangle"
    WHEN B+C <= A THEN "Not A Triangle"
    WHEN (A = B AND B = C) THEN "Equilateral"
    WHEN (A = B OR A = C OR B = C) THEN "Isosceles"
    WHEN (A != B AND B != C AND A != C) THEN "Scalene"
END
FROM TRIANGLES
