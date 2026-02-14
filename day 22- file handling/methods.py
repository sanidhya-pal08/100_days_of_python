fileeeee=open("synthetic.py",'w')
fileeeee.write("print('hello world')")
fileeeee.close()
lines=['line 1\n','line 2\n','line 3\n']
file=open("new_file.txt",'w')
file.writelines(lines)
file.close()
filee=open("new_file.txt")
while True:
    line=filee.readline()
    print(line)
    if not line:
        break

