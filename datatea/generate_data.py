#encoding: utf-8
__author__ = 'andy'

import os.path
from datetime import datetime

import config
import utils
import codecs

#定义转义字符串
transfer = {'<:>': '*luys*colon*', '<|>': "*luys*vline*"}
transferReturn = {'*luys*colon*': ':', '*luys*vline*': '|'}

#定义关键词对应函数
keyFunctionDict = {
    "fixed": str,
    "number": utils.getRandomInteger,
    "decimal": utils.getRandomDecimal,
    "dim": utils.getDimString,
    "regex": utils.getRegexString,
    "unique": utils.getUniqueRandomValue,
    "increase": utils.getIncreaseNumber,
    "file": utils.getValueFromFile,
    "comment": utils.getNullString
}

def genValueByConditons(conditions):
    """
    根据多个条件生成值
    """
    valueList = []
    for condition in conditions:
        valueList.append(unicode(genValueByConditon(condition)))
    return "".join(valueList)

def genValueByConditon(condition):
    """
    根据条件生成值
    """
    conditionList = [ utils.transferStr(value,**transferReturn).strip() for value in condition.split(":")]
    condtionName = conditionList.pop(0).strip().lower()
    global  keyFunctionDict
    if condtionName in keyFunctionDict.keys():
        return keyFunctionDict[condtionName](*conditionList)
    else:
        raise Exception(u"配置文件中的配置条件不正确！")

def generateData(fileName):
    print "start generate data ..."
    global dimStrings
    #获取字段配置信息
    columns = config.getDataConfigInfo(fileName)
    #获取维度配置信息
    utils.dimStrings = config.getDataDimConfigInfo(fileName)
    #获取一般配置信息
    commonConfig = config.getCommonConfigInfo(fileName)

    #获取基本配置信息
    colSeparator = commonConfig.get("column_separator")
    outputPath = commonConfig.get("ouput")
    fileName = commonConfig.get("filename").strip()

    #结果文件目录判断
    if(outputPath and not os.path.isdir(outputPath)):
        print outputPath , " is not a directory!"
        print "Generate the results at current directory!"
        outputPath=""
    elif( not outputPath):
        print "output path is null!"
        print "Generate the results at current directory!"
        outputPath=""

    outputFile = None

    try:
        #结果文件判断
        if(fileName):
            outputFile = codecs.open(outputPath + fileName + "_" + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'), "w", 'utf-8')
        else:
            outputFile = codecs.open(outputPath+'datatea_result_'+datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'), "w", 'utf-8')
        #开始生成数据
        for i in xrange(int(commonConfig.get("datanumbers").strip())):
            column = []
            for key in sorted(columns.keys()):
                column.append(genValueByConditons(utils.transferStr(columns[key], **transfer).split("|")))
            outputFile.write(colSeparator.join(column) + "\n")
    except Exception, e:
        print e
    finally:
        if(outputFile):
            outputFile.close()
        print "end!"
