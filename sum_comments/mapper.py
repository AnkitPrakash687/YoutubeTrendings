
import re
input_mapper = open("data_new.txt","r") # Opening data file in read-only mode
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
        x = re.search(r"[a-zA-Z0-9\s|]+", title)
        if x is None:
            title_clean = 'unknown character'
        else:
             title_clean = x.group()
             print(title_clean)
        # Writing video_id and dislikes to output file
        output_mapper.write(channel_title+","+comment_count+"\n")
        print(channel_title+","+comment_count+"\n")
        # printing video_id and dislikes to console
        #print(video_id+","+title_clean+","+dislikes+"\n")
# Closing all files
input_mapper.close()
output_mapper.close()
