#encoding: utf-8
__author__ = 'andy'
import random
import rstr
import uuid
import codecs

#自增数值计数器
incNum = None
#文件字典
filesMap = {}

#维度信息
dimStrings = {}

def getRegexString(regexString):
    """
    根据正则表达式，获取随机值
    """
    return rstr.xeger(regexString)

def getNullString(value):
    """
    返回空串
    """
    return ""

def getRandomInteger(lowNum, highNum):
    """
    获取随机整数
    """
    try:
        lowNum = int(lowNum)
        highNum = int(highNum)
    except:
        raise Exception(u"Error! getRandomInteger 类型转换错误！")
    if lowNum > highNum:
        lowNum, highNum = highNum, lowNum
    return random.randint(lowNum, highNum)

def getRandomDecimal(lowNum, highNum, digit):
    """
    获取随机小数
    """
    try:
        lowNum = int(lowNum)
        highNum = int(highNum)
        digit = int(digit)
    except:
        raise Exception(u"Error! getRandomDecimal 类型转换错误！")
    if lowNum > highNum:
        lowNum, highNum = highNum, lowNum
    return round(random.uniform(lowNum, highNum), digit)

def getUniqueRandomValue():
    """
    获取唯一值
    :return:
    """
    return uuid.uuid4().hex

def getDateTime(dateStr, formatStr):
    pass

def transferStr(input, **transfer):
    """
        转义字符串
    """
    output = input
    for key in transfer.keys():
        output = output.replace(key, transfer[key])
    return output

def increaseNumber(number, step):
    """
    根据部署的递增值
    """
    try:
        number = int(number)
        step = int(step)
    except Exception:
        raise Exception(u"Error! increaseNumber 类型转换错误！")
    result = number
    while 1:
        yield result
        result = result + step

def getIncreaseNumber(number, step):
    """
        获取递增值
    """
    global incNum
    if incNum is None:
        incNum = increaseNumber(number, step)
    return incNum.next()

def getDimString(dimName):
    """
    从维表获取字符串
    """
    global dimStrings
    dimStringList = dimStrings.get(dimName)
    return dimStringList[getRandomInteger(0, len(dimStringList)-1)]

def getValueFromFile(fileName, col, limit):
    """
    获取文件中一列的值
    """
    if int(col) <= 0:
        raise Exception(u"%s没有数据！" % fileName)
    resultList = []
    global filesMap
    if(filesMap.has_key(fileName+col)):
        resultList = filesMap.get(fileName+col, None)
    else:
        with codecs.open(fileName, 'r', 'utf-8') as valuesFile:
            line = "line"
            countNum = 0
            while line:
                countNum = countNum + 1
                if(limit is not None and limit < countNum):
                    break
                line = valuesFile.readline().strip()
                tmpList = line.split("\t")
                if(len(tmpList) < int(col)):
                    continue
                resultList.append(tmpList[int(col)-1])
            filesMap.update({fileName+col: resultList})
    return resultList[getRandomInteger(0, len(resultList)-1)]

if __name__ == "__main__":
    #transfer1 = {':': '*luys*colon*', '|': "*luys*vline*"}
    #transfer2 = {'*luys*colon*': '<:>', '*luys*vline*': '\|'}
    #print transferStr(transferStr("he\|llo|wo<:>\:rld\|", **transfer1),**transfer2)

    #transferStr("he\:llo|wo\|rld\|")
    # print getValueFromFile("values.txt", "3", 3)
    # a = getIncreaseNumber(1, 2)
    print getUniqueRandomValue()