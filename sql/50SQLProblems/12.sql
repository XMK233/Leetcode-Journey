/*
思路: 先弄出01课程分数小于60的, 然后跟student表合并, 然后再考虑排序的事情. 
*/

select * from student, sc
where 
	student.sid = sc.sid and
    sc.score < 60 and 
    sc.CId = "01"
order by score desc;

/*select student.*, sc.score from student, sc
where student.sid = sc.sid
and sc.score < 60
and cid = "01"
ORDER BY sc.score DESC;*/