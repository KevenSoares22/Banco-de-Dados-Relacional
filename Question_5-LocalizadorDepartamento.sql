select a.DEPARTMENT_NAME, count(b.DEPARTMENT_ID) as NUMBER_OF_EMPLOYEES
from departments as a
left join employees as b
on a.DEPARTMENT_ID = b.DEPARTMENT_ID

group by a.DEPARTMENT_ID
;