select student.SId,sname,ss from student,(
    select SId, AVG(score) as ss from sc  
    GROUP BY SId 
    HAVING AVG(score)> 60
    )r
where student.sid = r.sid;

-- 所有课平均成绩大于60分的学生的信息. 
-- 注意 avg, groupby, having的使用. 