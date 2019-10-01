i = open("USvideos.txt", "r")
o = open("output.txt", "w")

for line in i:
  data = line.strip().split(' ')
  # channel_title = data[4]
  # likes = data[7]   
  if (len(data) == 13):
    video_id,trending_date,title,channel_title,category_id,publish_time,views,likes,dislikes,comment_count,comments_disabled,ratings_disabled,video_error_or_removed = data
    o.write(channel_title + "\t" + likes+ "\n")
  # video_id, trending_date, title, channel_title, category_id, publish_time, tags, views, likes, dislikes, comment_count, thumbnail_link, comments_disabled, ratings_disabled, video_error_or_removed, description = data
  # o.write(channel_title + "\t" + likes+ "\n")
  print(channel_title + "\t" + likes+ "\n")

i.close()
o.close()
