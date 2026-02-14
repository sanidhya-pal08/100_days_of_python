with open("new_filee.txt",'w') as f:
    f.write("ehhhhhh")
    f.seek(3)
    f.truncate(3)
    # print((type(f)))
        # data=f.read(2)
    # print(data)
with open("new_filee.txt") as s:
    line=s.readline()
    print(line)
     