# Desc: 用于计算一个算式的值，并将算式中的数字和符号分别转换为列表和元组，最后将算式和结果转换为字典
import re
calculation= input("请输入一个用于计算的算式：")   
value = eval(calculation)
print(value)
symbol_list=re.split("\d+",calculation)   #将数字去掉，得到符号
del symbol_list[-1]
del symbol_list[0]
symbol_tuple=tuple(symbol_list)    #将符号转换为元组
print(symbol_tuple)

number_list=re.split(r"\+|\*|\-|\/",calculation)   #将符号去掉，得到数字
number_set=set(number_list)             #将数字转换为集合
number_list=list(number_set)            #将数字转换为列表
number_list.sort(reverse=True)      #将数字转换为列表并排序,从大到小
print(number_list)  

calculation_dict = {}               #将数字和符号转换为字典
calculation_dict[calculation] = value        #将算式和结果转换为字典
print(calculation_dict)