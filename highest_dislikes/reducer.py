s = open("output_mapper.txt","r")
r = open("output_reducer.txt", "w")

thisKey = ""
thisDislikes = 0

for line in s:
  data = line.strip().split(',')
  video_id, title, dislikes = data

  if video_id != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + title + '\t' + thisDislikes +'\n')
      thisDislikes = 0
      

    # start over when changing keys
    thisKey = video_id 
    
  
  # find and store max for the key
  if dislikes > thisDislikes:
      thisDislikes = dislikes
    
 

# output the final entry when done
r.write(thisKey + '\t' + title + '\t' + thisDislikes +'\n')

s.close()
r.close()