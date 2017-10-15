// https://www.hackerrank.com/challenges/earnings-of-employees

SELECT SALARY*MONTHS, COUNT(*) FROM EMPLOYEE WHERE SALARY*MONTHS = (SELECT MAX(SALARY*MONTHS) FROM EMPLOYEE)


