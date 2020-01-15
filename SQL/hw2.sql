use employees;

select first_name, last_name, title 
from employees inner join titles using(emp_no) limit 10;

select first_name, last_name, dept_name 
from employees inner join dept_manager using(emp_no) join departments using(dept_no) limit 10;