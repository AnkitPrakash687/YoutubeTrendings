mapperoutput = open("mapperoutput.txt","r") # Opening data file(output_mapper) in read only mode
reduceroutput = open("reduceroutput.txt", "w")  # Opening output_reducer file in write mode (It will create file if file doesnot exist)
lines = mapperoutput.readlines() # Reading each line from data and placing it in array
lines.sort() # sorting the array
dict = {} # creating an empty dictionary
# reading each line from array
for line in lines:
    # Seperating data by (,) and sending it to data array
    data = line.strip().split(',')
    channel_title = data[0] # Assigning data to variable
    try:
        comment_count = float(data[1])
        if channel_title in dict.keys():
            dict[channel_title] = dict[channel_title] + comment_count
        else:
            dict[channel_title] = 1
    except ValueError:
        continue
    
# Loop for readng dictionary 
for key,value in dict.items():
    # writing channel_title and total number of comments in output file
    reduceroutput.write("channel_title: "+key+","+"Total number of comments: "+str(value) +"\n")
    # Writing channel_title and total number of comments to console
    print("channel_title: "+key+","+"Total number of comments: "+str(value) +"\n")
# Closing all files
reduceroutput.close()
mapperoutput.close()