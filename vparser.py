##############################
# vcode parser
# create by wkk 2023_05_25
# update 2023_05_30
##############################
from vmodel import vmodel,pmodel

def str_split(line:str,sep:list)->list:
    target_str = ''
    for i in range(len(line)):
        if line[i] in sep:
            target_str+=' '
        else:
            target_str+=line[i]
    return target_str.split()

# parse parameter string
# parameter a = 512;
def param_parser(param_line)->pmodel:
    line_list = param_line.split()
    if line_list[0] != "parameter" or line_list[2] != "=":
        return None
    else:
        return pmodel(line_list[1],line_list[3][:-1] if line_list[3][0]==";" else line_list[3])


# parse port define string
# input a [3:0];
def port_parser(port_line)->vmodel:
    line_list = str_split(port_line,['[',':',']',','])
    if line_list[0] in [ "input","output"]:
        if len(line_list) < 4:
            return vmodel(line_list[0],None,None,line_list[1])
        else:
            return vmodel(line_list[0],line_list[1],line_list[2],line_list[3])
    else :
        return None

def module_name_parser(moduleline:str)->str:
    line_list = str_split(moduleline,['#','(',')'])
    if line_list[0] == "module":
        return line_list[1]
    else :
        return None
