
with open('test.txt') as f:
    f_content1 = f.read()
    print(f_content1)
    
    
count=0
for orderid in f_content1:
    count += 1
    if orderid == "usama":
        continue
    print("orderid{}: {}".format(count, orderid.strip()))


    