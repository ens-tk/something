f = open("9.txt") 
count=0 
rows=[i for i in f] 
rows_list = list(map(lambda x: x.split(';'), rows)) 
for raw in rows_list:
    raw_list = list(map(int, raw))
    if len(raw_list) - len(set(raw_list)) == 1:
        memory = []
        for value in raw_list:
            if value not in memory:
                memory.append(value)
                
            else:
                memory.remove(value)
                q = value
             
        avg = sum(memory)/len(memory)
        if avg <= q*2:
            count+=1
print(count)
