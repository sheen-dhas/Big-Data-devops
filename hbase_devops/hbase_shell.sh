#!/bin/sh

##cp spark-env.sh /home/build-spark/rootfs/usr/spark-2.2.0/conf
##chmod 777 spark-env.sh

cp trial.csv /home
chmod 777 trial.csv

##. /opt/hbase-server > a.out

apt-get -y update

apt-get install -y openssh-server

/opt/hbase/bin/start-hbase.sh

/opt/hbase/bin/hbase-daemons.sh start zookeeper

/opt/hbase-server


##/opt/hbase/bin/start-hbase.sh

# /opt/hbase/bin/zookeepers.sh start

##hbase shell

hbase shell ./sample_commands.txt
