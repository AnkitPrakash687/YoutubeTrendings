v_reducer = open("output.txt","r")
reduce_output = open("reduce_output.txt", "w")
lines = v_reducer.readlines()
lines.sort() 
max = 0
id = ''
dict = {} 
for line in lines:
    data = line.strip().split('/t')
    channel_title = data[0] 
    try:
        likes = float(data[1])
        if channel_title in dict.keys():
            dict[channel_title] = dict[channel_title] + likes
        else:
            dict[channel_title] = 1
    except ValueError:
        continue
   

for key,value in dict.items():
    likessum = sum(value)
    avglikes = likessum/len(value)
    reduce_output.write("channel_title: "+id+","+"Average number of likes: "+str(avglikes) +"\n")
    print("channel_title: "+id+","+"Average number of likes: "+str(avglikes) +"\n")
v_reducer.close()
reduce_output.close()