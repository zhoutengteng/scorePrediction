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




def writeClass(dic, record):
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
    peoples = {}
    #key表示班级编号
    for key in clas.keys():
        if key == "readme":
            continue
        classContentFile = open(listDirs["classes"][key])
        lines = classContentFile.readlines()
        courseName = lines[0].strip()
        homeworkSource = lines[1].strip()
        examSource = lines[2].strip()
        #line表示学生id
        for line in lines[3:]:
            line = line.strip()
            #可能有同学生id不同班级id, 还是合并算了
            # line =  line + key
            if not peoples.has_key(line):
                peoples[line] = {}
            if not peoples[line].has_key("selfId"):
                peoples[line]["selfId"] = line
            if peoples[line].has_key("classId"):
                peoples[line]["classId"] += "-" + key
            else:
                peoples[line]["classId"] = key

            if courseName == "程序设计 (II)":
                peoples[line]["courseCode2"] = courseName
            if courseName == "程序设计 (I)":
                peoples[line]["courseCode1"] = courseName
            if  peoples[line].has_key("homeworkSource"):
                peoples[line]["homeworkSource"] += "/" + homeworkSource
            else:
                peoples[line]["homeworkSource"] = homeworkSource
            if peoples[line].has_key("examSource"):
                peoples[line]["examSource"] += "/"  + examSource
            else:
                peoples[line]["examSource"] = examSource
            #获得作业多少题,和平均分  homeworkFile 是一周作业的几道题的综合, 实际是assgnments的集合
            homeworkFile = open(listDirs["homework"][homeworkSource])
            homeworkFile_lines = homeworkFile.readlines()
            homeworkFileTree = {}
            for homeworkFile_line in homeworkFile_lines:
                homeworkFile_line = homeworkFile_line.strip()
                homeworkFileTree[homeworkFile_line] = {}
                assignmentFile = open(listDirs["assignments"][homeworkFile_line])
                assignmentFile_lines = assignmentFile.readlines()
                exerciseId = assignmentFile_lines[0].strip()
                startTime = assignmentFile_lines[1].strip()
                hardDue = assignmentFile_lines[2].strip()
                softDue = assignmentFile_lines[3].strip()
                homeworkFileTree[homeworkFile_line]['exerciseId'] = exerciseId
                homeworkFileTree[homeworkFile_line]['assignmentId'] = exerciseId
                homeworkFileTree[homeworkFile_line]['startTime'] = startTime
                homeworkFileTree[homeworkFile_line]['hardDue'] = hardDue
                homeworkFileTree[homeworkFile_line]['softDue'] = softDue
                if homeworkFileTree[homeworkFile_line].has_key("count"):
                    homeworkFileTree[homeworkFile_line]["count"] += 1
                else:
                    homeworkFileTree[homeworkFile_line]["count"] = 1
                assignmentFile.close()

            allCount = 0
            d = {}
            if not peoples[line].has_key("assignmentids"):
                peoples[line]["assignmentids"] = []
            for homeworkFileTreeKey  in homeworkFileTree.keys():
                allCount += homeworkFileTree[homeworkFileTreeKey]["count"]
                peoples[line]["assignmentids"].append(homeworkFileTree[homeworkFileTreeKey]["assignmentId"])
            if peoples[line].has_key("homeworkAllNum"):
                peoples[line]["homeworkAllNum"] += allCount
            else:
                peoples[line]["homeworkAllNum"] = allCount
            homeworkFile.close()
        classContentFile.close()
        # 至此得到基本数据
        # submissionBests = {}
        # for submissionKey in listDirs['submissions'].keys():
        #     submissionsFile = open(listDirs['submissions'][submissionKey])
        #     submissionsFileLines = submissionsFile.readlines()
        #     studentId = submissionsFileLines[0].strip()
        #     assignmentId = submissionsFileLines[1].strip()
        #     submitTime = submissionsFileLines[2].strip()
        #     score = submissionsFileLines[3].strip()
        #     submissionsFile.close()
    writeClass(peoples, record)
    record.close()