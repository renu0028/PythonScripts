dictionary={"name":"Renu","age":21,"likes":"Painting"}
def sentence(name,age,likes):
 s="Hello {}!You are {} years old...and you like {}".format(name,age,likes)
 return s
print(sentence(**dictionary))
