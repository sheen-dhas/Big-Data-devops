#!/bin/sh


apt-get -y update

apt-get install -y openssh-server

/opt/hbase/bin/start-hbase.sh

/opt/hbase/bin/hbase-daemons.sh start zookeeper

/opt/hbase-server


##/opt/hbase/bin/start-hbase.sh

# /opt/hbase/bin/zookeepers.sh start

##hbase shell

hbase shell ./sample_commands.txt
