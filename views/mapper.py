
import re
input_mapper = open("./US_data.txt","r") # Opening data file in read-only mode
output_mapper = open("output_mapper.txt","w") # Opening output_mapper file in write mode (It will create file if file doesnot exist)
regex = "[a-zA-Z0-9\s|]+"

# For loop for reading each line from the text file
for line in input_mapper:
    # Seperating data by (,) and sending it to data array
    data = line.strip().split(',')
    # Checking the size of array
    if (len(data) == 14):
        # Assigning data to different variables
        video_id,trending_date,title,channel_title,category_id,publish_time,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed = data
        x = re.search(r"[a-zA-Z0-9\s|]+", channel_title)
        if x is None:
            channel_title_clean = 'unknown character'
        else:
             channel_title_clean = x.group()
             print(channel_title_clean)
        # Writing video_id and dislikes to output file
        output_mapper.write(channel_title_clean+","+views+"\n")
        # printing video_id and dislikes to console
        #print(video_id+","+title_clean+","+dislikes+"\n")
# Closing all files
input_mapper.close()
output_mapper.close()
