## you should remember:
## the alias of tables
## and use alias to do query. 

select e1.Name Employee from Employee e1 where e1.Salary > (select e2.Salary from Employee e2 where e2.Id = e1.ManagerId);