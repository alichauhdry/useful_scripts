import fileinput
import re
import sys

print sys.argv[0]
print sys.argv[1]
print sys.argv[2]

log_file_path = sys.argv[1]
new_log_file_path = sys.argv[2]


#regex = '[-+]?[0-9]+\:[-+]?[0-9]+\:[-+]?[0-9]+\:[-+]?[0-9]+$'
#regex = '(?:(?!\:)(?:.|\n))*\:(?:(?!\:)(?:.|\n))*\:(?:(?!\:)(?:.|\n))*\:'
regex = '[0-9]+\:[0-9]+\:[0-9]+(\.|\:)[0-9]+'
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
new_log_file = open (new_log_file_path, 'w')

new_log_file.writelines(file_buffer)

log_file.close()
new_log_file.close()
