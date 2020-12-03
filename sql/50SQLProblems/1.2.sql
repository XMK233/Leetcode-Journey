select * from 
(select * from sc where cid = "01") as t1
left join  
(select * from sc where cid = "02") as t2
on t1.sid = t2.sid;

-- 主要是学习一下join怎么写. 