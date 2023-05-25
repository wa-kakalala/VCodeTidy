##############################
# base store model
# create by wkk 2023_05_25
# update 2023_05_25
##############################

# store : parameter a = 512;
class pmodel:
    pin_name  = None
    pin_value = None
    
    def __init__(self,pin_name,pin_value):
        self.pin_name  = pin_name
        self.pin_value = pin_value

# store : input a [3:0];
class vmodel:
    pin_type   = None   # input or output
    range_up   = None   # [range_up:range_down]
    range_down = None
    pin_name   = None    

    def __init__(self,pin_type,range_up,range_down,pin_name):
        self.pin_type   = pin_type
        self.range_up   = range_up
        self.range_down = range_down
        self.pin_name   = pin_name

class port_list:
    pmodel_list  =  []
    vmodel_list  =  []

    def add_pmodel(self,pmodel):
        self.pmodel_list.append(pmodel)
    def add_vmodel(self,vmodel):
        self.vmodel_list.append(vmodel)
