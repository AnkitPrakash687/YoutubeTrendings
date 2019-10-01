input_reducer = open("output_mapper.txt","r") # Opening data file(output_mapper) in read only mode
output_reducer = open("output_reducer.txt", "w")  # Opening output_reducer file in write mode (It will create file if file doesnot exist)
lines = input_reducer.readlines() # Reading each line from data and placing it in array
lines.sort() # sorting the array
max = 0
id = ''
dict = {} # creating an empty dictionary
# reading each line from array
for line in lines:
    # Seperating data by (,) and sending it to data array
    data = line.strip().split(',')
    video_id = data[0] # Assigning data to variable
    try:
        dislikes = float(data[1])
        if video_id in dict.keys():
            dict[video_id] = dict[video_id] + dislikes
        else:
            dict[video_id] = 1
    except ValueError:
        continue
   
# Loop for readng dictionary
for key,value in dict.items():
    if(dict[key] >= max):
        max = dict[key]
        id = key

# writing video_id and total number of dislikes in output file
output_reducer.write("video_id: "+id+","+"Total number of dislikes: "+str(max) +"\n")
# Writing video_id and total number of  to console
print("video_id: "+id+","+"Total number of dislikes: "+str(max) +"\n")
# Closing all files
input_reducer.close()
output_reducer.close()