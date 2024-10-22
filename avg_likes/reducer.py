s = open("output.txt","r")
r = open("reducer_output.txt", "w")

thisKey = ""
thisLikes = 0
likes_sum = 0
likesCount = 0
likesAverage = 0.0
for line in s:
  data = line.strip().split(',')
  channel_title, likes = data

  if channel_title != thisKey:
    if thisKey:
      # output the last key value pair result
      print('The channel_title "'  + channel_title + '" has minimum likes of ' + thisLikes +'\n')
      r.write(thisKey + '\t' + thisLikes +'\n')
      thisLikes = 0
      

    # start over when changing keys
    thisKey = channel_title 
    
  
  # find and store max for the key
    if likes > thisLikes:
      thisLikes = likes
 
# output the final entry when done
print('The channel title "'  + channel_title + '" has minimum likes of ' + thisLikes +'\n')
r.write(thisKey + '\t' + thisLikes +'\n')

s.close()
r.close()