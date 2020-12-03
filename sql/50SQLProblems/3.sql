select student.* from 
(select distinct sid from sc) as t1, 
student
where student.sid = t1.sid;

-- 上面是我自己实现的. 感觉可能更有益于理解. 

/*select DISTINCT student.*
from student,sc
where student.SId=sc.SId*/