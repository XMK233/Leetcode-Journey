select a.cid, a.sid, a.score, count(b.score)+1 as rank
from sc as a 
left join sc as b 
on a.score < b.score and a.cid = b.cid
group by a.cid, a.sid, a.score
order by a.cid, rank ASC;

/*
这道题不是很懂. 得剖析一下才能理解. 
*/