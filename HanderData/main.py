#coding=utf-8
import os

#暂时用空格代替tab
def tab():
    return "    "

def mapL():
    mapList = [
        "selfId", "classId",  "sex" , "firstGoal" , "codeInHigh" , "scoreInHig" , "province" ,
        "courseCode1" , "courseCode2", "homeworkSource" , "examSource" ,
        "homeworkAllNum" , "homeworkYourNum" , "homeworkYourMeanScore" ,
        "MidtermSimualtionAllNum", "MidtermSimualtionYourNum" , "MidtermSimualtionYourScore" ,
        "MidtermAllNum" , "MidtermYourNum" , "MidtermYourScore" ,
        "SE122FinalSimualtionAllNum" , "SE122FinalSimualtionYourNum" , "SE122FinalSimualtionYourScore" ,
        "SE122FinalAllNum" , "SE122FinalYourNum" , "SE122FinalYourScore" ,
        "SE123MidtermAllNum" , "SE123MidtermYourNum" , "SE123MidtermYourScore" ,
        "SE123Final1AllNum" , "SE123Final1YourNum", "SE123Final1YourScore" ,
        "SE123Final2AllNum","SE123Final2YourNum","SE123Final2YourScore" ,
        "examMeanScore", "positionInClass"
    ]
    return mapList




def writeOneClass(dic, record):
    #print dic
    c = {}
    for people in dic.keys():
        for item in mapL():
            if dic[people].has_key(item):
                record.write(('{0: ^' + str(len(item)) + '}').format(dic[people][item]) + tab())
            else:
                record.write(('{0: ^' + str(len(item)) + '}').format("") + tab())
        record.write("\n")


if  __name__ == "__main__":
    basePath = '/Users/zhoutengteng/Downloads/2013'
    infoPeople = {}
    listDirs = {}
    for dir in os.listdir(basePath):
        if os.path.isdir(basePath + "/"+dir):
            listDirs[dir] = {}
            for file in os.listdir(basePath + "/" + dir):
                listDirs[dir][file] = basePath + "/" + dir + "/" + file
    # fp = open("preLoad.txt", "w")
    # fp.write(str(listDirs))

    record = open("record.csv", "w")
    record.write("selfId" + tab() + "classId" + tab() + "sex" + tab() + "firstGoal" + tab() +  "codeInHigh"+ tab() + "scoreInHig" + tab() + "province" + tab() +
                 "courseCode1" + tab() + "courseCode2" + tab() + "homeworkSource" + tab() + "examSource" + tab() +
                 "homeworkAllNum" + tab() + "homeworkYourNum" + tab() + "homeworkYourMeanScore" + tab() +
                 "MidtermSimualtionAllNum" + tab() + "MidtermSimualtionYourNum" + tab() + "MidtermSimualtionYourScore" + tab() +
                 "MidtermAllNum" + tab() + "MidtermYourNum" + tab() + "MidtermYourScore" + tab() +
                 "SE122FinalSimualtionAllNum" + tab() + "SE122FinalSimualtionYourNum" + tab() + "SE122FinalSimualtionYourScore" + tab() +
                 "SE122FinalAllNum" + tab() + "SE122FinalYourNum" + tab() + "SE122FinalYourScore" + tab() +
                 "SE123MidtermAllNum" + tab() + "SE123MidtermYourNum" + tab() + "SE123MidtermYourScore" + tab() +
                 "SE123Final1AllNum" + tab() + "SE123Final1YourNum" + tab() + "SE123Final1YourScore" + tab() +
                 "SE123Final2AllNum" + tab() + "SE123Final2YourNum" + tab() + "SE123Final2YourScore" + tab() +
                 "examMeanScore" + tab() + "positionInClass")
    record.write("\n")
    # {
    #   "classes": {
    #       "30275" : "---path---",
    #       "30265" : "---path---",

    #   },
    #   "students": {
    #       "30275" : "---path---"
    #   },
    # }
    clas = listDirs["classes"]
    for key in clas.keys():
        peoples = {}
        if key == "readme":
            continue
        classContentFile = open(listDirs["classes"][key])
        lines = classContentFile.readlines()
        courseName = lines[0].strip()
        homeworkSource = lines[1].strip()
        examSource = lines[2].strip()
        for line in lines[3:]:
            line = line.strip()
            peoples[line] = {}
            peoples[line]["selfId"] = line
            peoples[line]["classId"] = key
            if courseName == "程序设计 (II)":
                peoples[line]["courseCode2"] = courseName
            else:
                peoples[line]["courseCode2"] = "not exist"
            if courseName == "程序设计 (I)":
                peoples[line]["courseCode1"] = courseName
            else:
                peoples[line]["courseCode1"] = "not exist"
        writeOneClass(peoples, record)
        classContentFile.close()
    record.close()