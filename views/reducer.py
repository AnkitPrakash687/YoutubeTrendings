input_reducer = open("output_mapper.txt","r") # Opening data file(output_mapper) in read only mode
output_reducer = open("output_reducer.txt", "w")  # Opening output_reducer file in write mode (It will create file if file doesnot exist)
lines = input_reducer.readlines() # Reading each line from data and placing it in array
lines.sort() # sorting the array
dict = {} # creating an empty dictionary
# reading each line from array
for line in lines:
    # Seperating data by (,) and sending it to data array
    data = line.strip().split(',')
    channel_title = data[0] # Assigning data to variable
    try:
        views = float(data[1])
        if channel_title in dict.keys():
            dict[channel_title] = dict[channel_title] + views
        else:
            dict[channel_title] = 1
    except ValueError:
        continue
    
# Loop for readng dictionary 
for key,value in dict.items():
    # writing channel_title and total number of suicide in output file
    output_reducer.write("channel_title: "+key+","+"Total number of suicides: "+str(value) +"\n")
    # Writing channel_title and total number of suicides to console
    print("channel_title: "+key+","+"Total number of suicides: "+str(value) +"\n")
# Closing all files
input_reducer.close()
output_reducer.close()