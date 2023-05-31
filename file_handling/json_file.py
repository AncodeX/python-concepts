import json


friends = [
    {"name": "joe", "nickname": "joe123"},
    {"name": "michaell", "nickname": "michaell123"},
    {"name": "victor", "nickname": "victor123"},
    {"name": "daniel", "nickname": "daniel123"},
]   

friends_json = json.dumps(friends)
print(friends_json) 


with open(file="file_handling/file.json", mode="w", encoding="UTF-8") as file:
    json.dump(obj=friends, fp=file, indent=2, ensure_ascii=True)

with open(file="file_handling/file.json", mode="r", encoding="UTF-8") as file:
    file_json = json.load(file)
    for j in file_json:
        print(j["name"], j["nickname"])