classDict = {
    "class" : {
        "student": {
            "name": "Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}
print(classDict["class"]["student"]["name"])
classDict["class"]["student"]["marks"]["physics"]=89
classDict["class"]["student"]["marks"]["moyenne"]=sum(classDict["class"]["student"]["marks"].values())/2
classDict["class"]["student"] = [{"name":"Mike","marks":classDict["class"]["student"]["marks"]}]
classDict["class"]["student"].append({"name":"Ted","marks":{"physics":34,"history":99,"moyenne":66.5}})
classDict["class"]["average_grade"]=sum(u["marks"]["moyenne"] for u in classDict["class"]["student"])/len(classDict["class"]["student"])
print(classDict["class"]["student"])
print(classDict)