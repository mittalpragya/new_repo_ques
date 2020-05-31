#!/bin/bash

DATE_TODAY=$(date +"%Y_%m_%d")
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=kranti@123
DB_NAME=My_Test
SQL_EXT=sql
BACKUP_DIRECTORY=/home/pragya/dumps/
DESTINATION_LOCATION=$(pwd)/
DB_DUMP=$BACKUP_DIRECTORY$DB_NAME-$DATE_TODAY.sql



# From master branch make a new branch on git call it YYYY_MM_DD

git branch $DATE_TODAY

# Checkout the new branch

git checkout $DATE_TODAY

# Create a My SQL Dump of your DB

mysqldump -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME >$BACKUP_DIRECTORY$DB_NAME-$DATE_TODAY.sql

# Push this file to the branch you created

cp $DB_DUMP $DESTINATION_LOCATION

# Now Push all the code you have to this branch

git push -u origin $DATE_TODAY
git add .
git commit -m "My branch code"
git push origin master
