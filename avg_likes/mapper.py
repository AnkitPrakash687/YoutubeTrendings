v_input = open("./data/usvideos_v.txt", "r")
v_output = open("output.txt", "w")

for line in v_input:
    data = line.strip().split('/t')   
    if (len(data) == 2):
        channel_title,likes = data
        v_output.write(channel_title + "\t" + likes+ "\n")
        print(channel_title + "\t" + likes+ "\n")

v_input.close()
v_output.close()