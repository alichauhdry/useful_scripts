#!/usr/bin/env python

import fileinput
import re
import sys

log_file_path = sys.argv[1]

#regex = '[-+]?[0-9]+\:[-+]?[0-9]+\:[-+]?[0-9]+\:[-+]?[0-9]+$'
#regex = '[0-9]+\:[0-9]+\:[0-9]+(\.|\:)[0-9]+' #For time stamps not for dates
#regex = '0x[0-9]{0,3}([a-z]|[A-Z]|[0-9]){0,4}' #For memory addresses
#regex = '\s[0-9].[0-9]{6}\sms' #For timespan

print ("Ready to remove extra stuff in file: %s" % log_file_path)

regex = '((=\s[0-9]{0,3}.[0-9]{6,10}\sms)|(0x[0-9]{0,3}([a-z]|[A-Z]|[0-9]){0,4})|([0-9]+\:[0-9]+\:[0-9]+(\.|\:)[0-9]+))'

pattern = re.compile(regex)

log_file = open(log_file_path,'r')

file_buffer = []

flag = 0
for line in log_file:
 file_buffer.append(re.sub(pattern,'',line))
 if (pattern.search(line) != None):
  flag = flag + 1

new_log_file_name = log_file_path+"_parsed"

new_log_file = open (new_log_file_name, 'w')

new_log_file.writelines(file_buffer)

log_file.close()
new_log_file.close()

print ("Total alterations have been done under file name: '%s' are: %d" % (new_log_file_name,flag))
print ("DONE")
