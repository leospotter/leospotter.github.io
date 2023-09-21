import os
path_to_pictures = "Media/pictures/"
path_to_js = "display_pictures.js"

# renames pictures to p1, p2, p3
i = 0
for filename in os.listdir(path_to_pictures):
    i += 1
    new_name = "reset" + str(i) + ".jpeg"
    os.rename(path_to_pictures + filename, path_to_pictures + new_name)
    
i = 0
for filename in os.listdir(path_to_pictures):
    i += 1
    new_name = "p" + str(i) + ".jpeg"
    os.rename(path_to_pictures + filename, path_to_pictures + new_name)    
    
    
with open(path_to_js, "r") as jscode:
    content = jscode.read()
    content = content[:17] + str(i) + content[18:]

with open(path_to_js, "w") as jscode:
    jscode.write(content)
    