############################
# 数据生成工具 datatea 1.0
# 日期： 2014/04/28
# 作者： luys
############################

******************************
 datatea1.0
    依赖包：rstr-2.1.2
******************************
运行方式： python run.py --data 配置文件(utf-8格式的文件)
        例如： python run.py --data config/data.json
*************************************
--data的配置文件(json文件)说明：
    基本样式：
        {
            "common":{},
            "columns":{},
            "dim_string":{}
        }
    common配置说明：
        "datanumbers": "10",  #数据条数
        "column_separator": ";", #字段间隔
        "ouput": "/home/hostname/", #生成文件的目录（可选）默认是当前运行目录
        "filename": "mytest" #生成文件的名称（可选） 不填会生成一个随机文件

    columns配置说明：
        基本配置名称: "字段编号": "规则名: 规则1|规则名: 规则2"
            例如："column001": "fixed: 111| number:2:3"
                "column001": "fixed: 111| number:2:3"
    dim_string配置说明：
        基本格式是: "名称": "可选值1|可选值2..."
            例如：
                "dim_name": "value1|value2|value3",
                "dim_name2": "value1|value2|value3",

    columns中的规则说明：
        fixed  固定值,配置规则： fixed: value  如： fixed:11 ,返回的字符串就是 11, 注意fixed不会做去空操作，所以如果11前后有空格，则最终结果也会包含空格
        number 随机整数, 配置规则：number:left:right 如：number:2:6, 返回2-6之间的随机整数
        increase  递增值, 配置规则: increase:number:step  如：increase:1:2，则返回 1 3 5 ..等的递增数
        decimal 随机小数,配置规则： decimal:left:right:digit 如： decimal:1:2:3, 返回1-2之间的小数并保留3位小数
        dim 从dim_string的配置中随机取值, 配置规则： dim: dim_name，如:dim:dim_name1, 返回在dim_string配置的dim_name1的值中，随机挑选的一个值
        regex 根据正则返回一个字符串, 配置规则： regex: 正则表达式， 如: regex: [A-Z]\\d[a-z]\\d[A-Z]\\d, 返回一个符合正则表达式的值如：T0q5E6
        unique  产生一个不重复的随机36位字符串，配置规则： unique   如： unique
        file    通过文件获取值。配置规则： file: filepath:column:limit, filepath:路径，column:第几列（列必须以tab键分割）, limit限制取多少行
        comment 对字段的一个注释说明，不返回任何值
        |  规则连接符，可以将多个规则返回值合并成一个字符串返回：如： fixed: 11|number:2:6 ，可以返回115
        如果配置值中包含|或者:, 请用<|>或者<:>进行转义 （注：DIM中不能使用<|>和<:>）
*************************************