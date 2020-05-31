#!/usr/bin/env python3

import os
from datetime import datetime

DATE_TODAY = datetime.now().strftime("%Y_%m_%d")
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = 'kranti@123'
DB_NAME = 'My_Test'
BACKUP_DIRECTORY = '/home/pragya/dumps/'
DESTINATION_LOCATION = os.getcwd() + '/'
DB_DUMP = BACKUP_DIRECTORY + DB_NAME + '-' + DATE_TODAY + '.sql'

# From master branch make a new branch on git call it YYYY_MM_DD

os.system("git branch " + DATE_TODAY)

# Checkout the new branch

os.system("git checkout " + DATE_TODAY)

# Create a My SQL Dump of your DB

os.system("mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_PASSWORD + " " + DB_NAME + " >" + DB_DUMP)

# Push this file to the branch you created

os.system("cp " + DB_DUMP + " " + DESTINATION_LOCATION)

# Now Push all the code you have to this branch

os.system("git push -u origin " + DATE_TODAY)
os.system("git add .")
os.system("git commit -m 'My branch code'")
# git push -u origin $DATE_TODAY
# git add .
# git commit -m "My branch code"
# git push origin master
#
