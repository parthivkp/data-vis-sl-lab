declare
cursor cmp is
select * from part;
emp cmp%rowtype;
begin 
 open cmp;
 loop
 fetch cmp into emp;

 exit when cmp%notfound;
dbms_output.put_line(emp.PNO||' '||emp.PNAME||EMP.COLOUR);
END LOOP;
close cmp;

end;
/
 
