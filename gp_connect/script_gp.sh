

su gpadmin /usr/local/greenplum-db/bin/gpstate	
su gpadmin /usr/local/greenplum-db/bin/psql -c "select current_date" > /home/gpadmin/date_tst.log
echo /home/gpadmin/date_tst.log
exit ;		
