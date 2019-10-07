s = open("output_mapper.txt","r")
r = open("output_reducer.txt", "w")

thisKey = ""
total = 0
lines = s.readlines()
lines.sort()
for line in lines:
  data = line.strip().split(',')
  channel_title, views = data

  if channel_title != thisKey:
    if thisKey:
      # output the last key value pair result
        print('The channel "'  + channel_title + '" has total views of ' + str(total) +'\n')
        r.write(channel_title + ',' + str(total)+'\n')
        total = 0
      

    # start over when changing keys
    thisKey = channel_title 
    
  
  # find and store max for the key
    total += int(views)
    
 

# output the final entry when done
print('The channel "'  + channel_title + '" has total views of ' + str(total) +'\n')
r.write(channel_title + ',' + str(total)+'\n')

s.close()
r.close()
