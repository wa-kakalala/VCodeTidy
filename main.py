from vparser import param_parser,port_parser,module_name_parser
from vmodel import port_list

vcode = '''module spi_tx # (
    parameter CPOL          =    1'b0        ,        // clock polarity
    parameter CPHA          =    1'b0        ,        //      clock phase -> simple time
    parameter MAX_COUNT     =       3        ,
    parameter COUNT_BITS    =       12
)(
              input           i_clk                   ,
     input           i_rst_n                 ,
    input  [7      :0        ]    i_tx_data               ,
    input           i_tx_data_valid         ,
    output          o_spi_tx                ,
    output          o_spi_clk               ,
    output          o_spi_cs_n              ,
    output          o_spi_busy              
);'''

## format line string
# - no space begin
# - keep one space distance
# - between [ and ] with no space
def remove_more_space(line : str)->str:
    space = False
    allowSpace = True
    line = line.strip()
    newline = ""
    hasDot  = False
    for ch in line:
        if ( space or not allowSpace)  and ch ==' ':
            space = True
            continue
        elif not space and ch==' ':
            newline += ' '
            space = True
            continue
        elif ch == '[':
            allowSpace = False
        elif ch == '.':
            allowSpace = False
            hasDot = True
        elif ch == ']':
            allowSpace = True 
        elif hasDot:
            allowSpace = True
            hasDot = False
        space = False
        newline += ch
    return newline




if __name__ == "__main__":
    vcode_model = port_list()
    vcode_line = vcode.split("\n")
    for line in vcode_line :
        if "module" in line:
            vcode_model.module_name = module_name_parser(line)
        elif "parameter" in line:
            vcode_model.pmodel_list.append(param_parser(line))
        elif "input" in line or "output" in line:
            vcode_model.vmodel_list.append(port_parser(line))
        else:
            continue

    print("module {} # (".format(vcode_model.module_name))
    for param in vcode_model.pmodel_list[:-1]:
        print("  parameter\t{: <16}=\t{}\t\t\t,".format(param.pin_name,param.pin_value))
    param = vcode_model.pmodel_list[-1]
    print("  parameter\t{: <16}=\t{}\t\t\t".format(param.pin_name,param.pin_value))
    print(")(")
    for port in vcode_model.vmodel_list[:-1]:
        if port.range_down is None:
            print("  {: <16}{: <10}\t,".format(port.pin_type,port.pin_name))
        else:
            print("  {}\t[{}:{}]\t\t{}\t,".format(port.pin_type,port.range_up,port.range_down,port.pin_name))
    port = vcode_model.vmodel_list[-1]
    if port.range_down is None:
        print("  {: <8}{: <4}\t".format(port.pin_type,port.pin_name))
    else:
        print("  {}\t[{}:{}]\t\t{}\t".format(port.pin_type,port.range_up,port.range_down,port.pin_name))
    print(");")

    width = 10
        



