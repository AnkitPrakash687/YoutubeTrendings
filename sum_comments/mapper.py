input_mapper = open("../data/USvideos.txt","r") # Opening data file in read-only mode 
output_mapper = open("mapperoutput.txt","w") # Opening output_mapper file in write mode (It will create file if file doesnot exist)
# For loop for reading each line from the text file
for line in input_mapper:
    # Seperating data by (,) and sending it to data array
    data = line.strip().split(',')
    # Checking the size of array
    if (len(data) == 16):
        # Assigning data to different variables
        video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,dummy = data
        # Writing channel_title and views to output file
        output_mapper.write(channel_title+","+comment_count+"\n")
        # printing channel_title and views to console
        print(channel_title+","+comment_count+"\n")
# Closing all files
input_mapper.close()
output_mapper.close()