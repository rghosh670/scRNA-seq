import json

with open('data/muscleTFStuff/clusterBasedOnPearson.txt') as json_file:
    x = json.load(json_file)
json_file.close()

with open('data/muscleTFStuff/wardClusterDict.txt') as json_file:
    y = json.load(json_file)
json_file.close()

shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
print(len(shared_items))


# def common_member(a, b):
#     a_set = set(a)
#     b_set = set(b)

#     # check length
#     if len(a_set.intersection(b_set)) > 0:
#         return(a_set.intersection(b_set))
#     else:
#         return("no common elements")

# print(len(common_member(x, y)))