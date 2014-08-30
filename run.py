#encoding: utf-8
__author__ = 'andy'
import sys
import os.path

from datatea import generate_data
from datatea import compare_structure

#输入限制
argLimits = ["--data", "--structure"]

def analysisInputArgs(args):
    """
        解析输入参数，参数只能是输入限制中配置的参数。
        输入： args；输出： dict。
    """
    results = {}
    if(len(args) == 1):
        print u"请输入参数! " + u" or ".join(argLimits)
        sys.exit(1)
    if(len(args) % 2 != 1):
        print u"输入参数不正确!" + u" or ".join(argLimits)
        sys.exit(1)
    for argsIndex in xrange(len(args[1:])):
        if (argsIndex % 2 == 0):
            key = args[1:][argsIndex]
            if key not in argLimits:
                print u"输入参数不正确!"  + " or ".join(argLimits)
                sys.exit(1)
        else:
            val = args[1:][argsIndex]
            results.update({key: val})
    return results

#读取表结构文件配置信息
def readStructureConfig(typeFile, dbFile, schemaFile, tableFile):
    print u"功能尚未实现"
    sys.exit(0)

if __name__ == "__main__":
    configPath = analysisInputArgs(sys.argv)

    if(configPath.has_key("--data") and os.path.isfile(configPath["--data"])):
        try:
            generate_data.generateData(configPath["--data"])
        except Exception, e:
            print e
    elif(configPath.has_key("--structure") and os.path.isfile(configPath["--structure"])):
        try:
            compare_structure.compareStructure(configPath["--structure"])
        except Exception, e:
            print e
    else:
        print "%s not exits!" % (configPath[configPath.keys().pop()])
        sys.exit(1)