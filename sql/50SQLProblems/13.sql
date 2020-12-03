/*
先求所有学生的平均成绩
*/
select * from sc, 
(select sid, avg(score) as avgscore from sc
group by sid) tmp 
where sc.sid = tmp.sid
order by avgscore desc;