import encodings
import json
colours={
    "Red" : "Kirmizi",
    "White" : "Beyaz",
    "Yellow" : "Sari",
    "Orange" : "Turuncu"
}

with open("colours.jason","w") as f :
    json.dump(colours,f,ensure_ascii=False,indent=4)

with open("colours.jason","r",encoding="utf-8") as f:
    data=json.load(f)
 

print(data)

#write text line by line
colours=["re","green","nlue","orange"]
with open("colours.txt","w",encodings="utf-8") as f:
    f.write("hello world"+"\n")
    for color in colours:
        f.write(color + "\n")