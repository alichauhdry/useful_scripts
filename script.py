import fileinput
import re
import sys

log_file_path = sys.argv[1]
#new_log_file_path = sys.argv[2]


#regex = '[-+]?[0-9]+\:[-+]?[0-9]+\:[-+]?[0-9]+\:[-+]?[0-9]+$'
#regex = '[0-9]+\:[0-9]+\:[0-9]+(\.|\:)[0-9]+'
#regex = '0x[0-9]{0,3}([a-z]|[A-Z]|[0-9]){0,4}'
#regex = '\s[0-9].[0-9]{6}\sms'

regex = '((=\s[0-9]{0,3}.[0-9]{6,10}\sms)|(0x[0-9]{0,3}([a-z]|[A-Z]|[0-9]){0,4})|([0-9]+\:[0-9]+\:[0-9]+(\.|\:)[0-9]+))'

pattern = re.compile(regex)

#log_file_path = '/home/ezchaal/a_id.out'

log_file = open(log_file_path,'r')

file_buffer = []

#log_file_in_buffer = log_file.readline()
for line in log_file:
 file_buffer.append(re.sub(pattern,'',line))
 if pattern.search(line) is not None:
  print line
#print(re.sub(pattern,'',line))
  

#if re.match(pattern,line) is not None:
  #print line
 
#new_log_file_path = '/home/ezchaal/sample_id.parsed'
new_log_file = open (log_file_path+"_parsed", 'w')

new_log_file.writelines(file_buffer)

log_file.close()
new_log_file.close()
