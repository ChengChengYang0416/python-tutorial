# file operation
file = open("data.txt", mode = "w")         # open a file
file.write("Hello world!\nHello world!")    # write something to file
file.close()                                # close the file

# best practice, without closing the file
with open("test.txt", mode = "w") as file:
    file.write("This is a test.")

# read something from file
with open("point.txt", mode = "r") as re_from_data:
    data = re_from_data.read()
print(data)

# read and write file from json file
import json
with open("config.json", mode = "r") as json_file:
    data = json.load(json_file)
print(data)
data["name"] = "New Name"
print(data)
with open("config.json", mode = "w") as json_file:
    json.dump(data, json_file)