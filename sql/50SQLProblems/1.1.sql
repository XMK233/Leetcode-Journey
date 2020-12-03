/* select * from 
    (select * from sc where sc.CId = '01') as t1, 
    (select * from sc where sc.CId = '02') as t2
where t1.SId = t2.SId; */

select * from 
	(select * from sc where cid = "01") as t1, 
	(select * from sc where cid = "02") as t2
where t1.sid = t2.sid;

-- 别忘了, t1和t2之间没有加逗号隔开, 这个就会出问题的. 