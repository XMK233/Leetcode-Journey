select * from student 
where student.sid in (select sid from sc);

select * from student
where exists (select * from sc where student.sid = sc.sid)