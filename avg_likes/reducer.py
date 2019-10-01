s = open("output.txt","r")
r = open("r.txt", "w")
lines = s.readlines()
lines.sort() 
max = 0
id = ''
dict = {} 
for line in lines:
    data = line.strip().split(',')
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

r.write("channel_title: "+id+","+"Average number of likes: "+str(avglikes) +"\n")
print("channel_title: "+id+","+"Average number of likes: "+str(avglikes) +"\n")
s.close()
r.close()