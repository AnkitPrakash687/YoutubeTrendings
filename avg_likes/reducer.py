s = open("output_new.txt","r")
r = open("r.txt", "w")

thisKey = ""
thisValue = 0
sum = 0

for line in s:
  data = line.strip().split(',')
  channel_id, likes = data

  if channel_id != thisKey:
    if thisKey:
      # output the last key value pair result
      print('The channel "'  + channel_id + '" has average likes of ' + thisValue +'\n')
      r.write(thisKey + '\t' + channel_id + '\t' + thisValue +'\n')
      thisValue = 0
      # r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = channel_id 
    # thisValue = 0.0
  
  # apply the aggregation function
    thisValue += float(likes)


# output the final entry when done
print('The channel "'  + channel_id + '" has average likes of ' + thisValue +'\n')
r.write(thisKey + '\t' + channel_id + '\t' + thisValue +'\n')

# r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()