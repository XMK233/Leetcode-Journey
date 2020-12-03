select * from student
where student.sid not in (
  select sc.sid from sc
  group by sc.sid
  having count(sc.cid)= (select count(cid) from course)
);