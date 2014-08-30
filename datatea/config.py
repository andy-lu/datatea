#encoding: utf-8
__author__ = 'andy'

import json
import sys

def getCommonConfigInfo(fileName):
    """
        根据配置文件，获得基本配置信息.
        输入： 配置文件； 输出： 数据配置信息
    """
    common = {}
    jsonFile = ""
    try:
        jsonFile = file(fileName)
        jsonString = json.load(jsonFile)
        common = jsonString.get('common')
        jsonFile.close()
    except Exception, e:
        print "getCommonConfigInfo, error", e.message
        sys.exit(1)
    finally:
        if(jsonFile):
            jsonFile.close()
    return common

def getDataConfigInfo(fileName):
    """
        根据数据配置文件，获得数据配置信息.
        输入： 配置文件； 输出： 字段配置信息
    """
    jsonFile = ""
    columns = {}
    try:
        jsonFile = file(fileName)
        jsonString = json.load(jsonFile)
        columns = jsonString.get('columns')
        jsonFile.close()
    except Exception, e:
        print "Error! 获取字段配置信息出错！ ", e
        sys.exit(1)
    finally:
        if(jsonFile):
            jsonFile.close()
    return columns

def getDataDimConfigInfo(fileName):
    """
        根据数据配置文件，获得维度数据信息.
        输入： 配置文件； 输出： 维度数据信息
    """
    dimStrings = {}
    jsonFile = ""
    try:
        jsonFile = file(fileName)
        jsonString = json.load(jsonFile)
        dimStrings = jsonString.get('dim_string')
        for key, value in dimStrings.iteritems():
            dimStrings[key] = value.split("|")
    except Exception, e:
        print "Error! 获取维度数据信息出错！", e.message
        sys.exit(1)
    finally:
        if(jsonFile):
            jsonFile.close()
    return dimStrings

def getStructureDBInfo(filename):
    """
        根据结构配置文件，获得数据库配置信息.
        输入： 配置文件； 输出： 数据库配置信息
    """
    jsonFile = ""
    databases = {}
    try:
        jsonFile = file(filename)
        jsonString = json.load(jsonFile)
        databases = jsonString.get('databases')
        jsonFile.close()
    except Exception, e:
        print "Error! 获取数据库配置信息出错！", e.message
        sys.exit(1)
    finally:
        if(jsonFile):
            jsonFile.close()
    return databases

def getStructureColTypeInfo(filename):
    """
        根据结构配置文件，获得数据库字段类型信息.
        输入： 配置文件； 输出： 数据库字段类型信息
    """
    jsonFile = ""
    columnType = {}
    try:
        jsonFile = file(filename)
        jsonString = json.load(jsonFile)
        columnType = jsonString.get('column_type')
        jsonFile.close()
    except Exception, e:
        print "Error! 获取数据库字段类型信息出错！", e
        sys.exit(1)
    finally:
        if(jsonFile):
            jsonFile.close()
    return columnType
