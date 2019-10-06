mapperoutput = open("output_mapper.txt","r") # Opening data file(output_mapper) in read only mode
reducer_output = open("reduceroutput.txt", "w")  # Opening output_reducer file in write mode (It will create file if file doesnot exist)
lines = mapperoutput.readlines() # Reading each line from data and placing it in array
lines.sort() # sorting the array
thisKey = ""
# reading each line from array
for line in lines:
 data = line.strip().split(',')
 channel_title,comment_count = data
 if channel_title != thisKey:
   if thisKey:
     # output the last key value pair result
     reducer_output.write(thisKey + '\t' + str(thisValue)+'\n')

   # start over when changing keys
   thisKey = channel_title
   thisValue = 0.0
 # apply the aggregation function
 thisValue += float(comment_count)

