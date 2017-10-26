

/usr/local/greenplum-db/bin/gpstate	
/usr/local/greenplum-db/bin/psql -c "select current_date" > /home/gpadmin/date_tst.log
cat /home/gpadmin/date_tst.log
exit ;		
