declare





begin

update supply
set quantity=quantity+(quantity*2);
dbms_output.put_line(sql%rowcount||'row were update');








end;
/