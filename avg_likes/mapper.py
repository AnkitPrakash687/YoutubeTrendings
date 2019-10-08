import re
v_input = open("./US_data.txt", "r")
v_output = open("output_new.txt", "w")
regex = "[a-zA-Z0-9\s|]+"

for line in v_input:
    data = line.strip().split(',')   
    if (len(data) == 14):
        video_id,trending_date,title,channel_title,category_id,publish_time,\
        views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed = data
        x = re.search(r"[a-zA-Z0-9\s|]+", title)
        if x is None:
          channel_p = 'unknown character'
        else:
          channel_p = x.group()
          # print(channel_p)        
        v_output.write(channel_title + "," + likes+ "\n")
        print(channel_title + "," + likes+ "\n")

v_input.close()
v_output.close()
