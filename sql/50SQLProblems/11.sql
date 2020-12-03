select student.sid, student.Sname, tmp.avgsc
from student, 
		(select sid, avg(score) as avgsc from sc
		where sid in 
				(select sid from sc where score < 60 group by sid having count(score) >= 2)
		group by sid) tmp
where student.sid = tmp.sid;