select student.sid, student.sname,r.coursenumber,r.scoresum
from student,
(select sc.sid, sum(sc.score) as scoresum, count(sc.cid) as coursenumber from sc 
group by sc.sid)r
where student.sid = r.sid;