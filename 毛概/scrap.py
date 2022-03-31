from bs4 import BeautifulSoup

hashSet = set()

for i in range(20):

    fileName = "test_" + str(i) + ".html"

    #print(fileName)

    saveAsName = "QuestionLists.txt"

    with open(fileName, "r", encoding="utf-8") as f:
        doc = BeautifulSoup(f, "html.parser")
    
        contentList = doc.find_all("li", class_="clearfix read")
        with open(saveAsName, "a+") as file:
            for content in contentList:
                title = content.find("div", class_="vtbegenerated inlineVtbegenerated")

                # 去重
                if title.text in hashSet:
                    continue
                hashSet.add(title.text)

                file.write(title.text + '\n')
                selection = content.find_all("div", class_="reviewQuestionsAnswerDiv")
                for eachSelect in selection:
                    # 判断题型

                    # 如果是选项栏直接跳过
                    if ("未给定" in eachSelect.text):
                        continue

                    # 如果是选择题
                    choiceList = eachSelect.find("div", class_="vtbegenerated inlineVtbegenerated")
                    if (choiceList != None):
                        # 判断是否正确
                        isRightAns = eachSelect.find("span", class_="correctAnswerFlag")
                        if (isRightAns != None):
                            file.write("[√]")
                        else:
                            file.write("[×]")
                        file.write(choiceList.text + '\n')
                        continue

                    # 如果是判断题
                    isJudge = "对" in eachSelect.text
                    if (isJudge == True):
                        eachSelect.find("span", class_="answerTextSpan")
                        # 判断正确与否
                        isRightAns = eachSelect.find("span", class_="correctAnswerFlag")
                        if (isRightAns != None):
                            file.write("[√]" + '\n')
                        else:
                            file.write("[×]" + '\n')
                file.write('\n')

