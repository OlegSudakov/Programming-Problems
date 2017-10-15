// https://www.hackerrank.com/challenges/the-blunder

SELECT CEIL(ABS((AVG(1.0*CONVERT(REPLACE(CONVERT(SALARY, CHAR),"0",""), UNSIGNED INTEGER))-AVG(1.0*SALARY)))) FROM EMPLOYEES
