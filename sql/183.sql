## you should remember:
## join the tables. 
## and "is null". At first you use "= null" and it returns nothing.  

select Customers.Name Customers from Customers left join Orders on Customers.Id = Orders.CustomerId where  Orders.Id is null;