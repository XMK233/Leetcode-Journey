select course.cname, tmp.* from course, (
select sc.CId ,
max(sc.score)as 最高分,
min(sc.score)as 最低分,
AVG(sc.score)as 平均分,
count(*)as 选修人数,
sum(case when sc.score>=60 then 1 else 0 end )/count(*)as 及格率,
sum(case when sc.score>=70 and sc.score<80 then 1 else 0 end )/count(*)as 中等率,
sum(case when sc.score>=80 and sc.score<90 then 1 else 0 end )/count(*)as 优良率,
sum(case when sc.score>=90 then 1 else 0 end )/count(*)as 优秀率 
from sc
GROUP BY sc.CId
ORDER BY count(*)DESC, sc.CId ASC) tmp 
where course.CId = tmp.cid
;
/*
直接抄了. 他直接用了sc, 没有结合其他的表. 
但是显然, 这个答案没有做完这一题. 因为这一题还包含了一个获得课程名字的部分, 他没有实现. 
*/