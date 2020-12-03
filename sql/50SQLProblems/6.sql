select student.* from student, teacher, course, sc
where (student.sid = sc.sid) and (course.cid=sc.cid) and (course.tid = teacher.tid) and (tname = 'Zhang San');