select * from sc
where sc.SId not in (
    select SId from sc 
    where sc.CId = '01'
) 
AND sc.CId= '02';