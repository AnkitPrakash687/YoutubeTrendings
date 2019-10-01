i = open("../data/USvideos.txt", "r")
o = open("output.txt", "w")

for line in i:
    data = line.strip().split(',')   
    if (len(data) == 16):
    video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,dummy = data
    o.write(channel_title + "\t" + likes+ "\n")
    print(channel_title + "\t" + likes+ "\n")

i.close()
o.close()
