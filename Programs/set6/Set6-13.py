import time
file_var=open('test_file.txt','r')
for line in file_var:
    print(line)
    time.sleep(1)
file_var.close()
