import os 

new_file = open("copy.txt", "w")
with open("orig.txt", "r") as f:
    new_file.write(f.read())

new_file.close()