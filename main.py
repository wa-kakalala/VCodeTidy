vcode = '''module spi_tx # (
    parameter CPOL          =    1'b0        ,        // clock polarity
    parameter CPHA          =    1'b0        ,        //      clock phase -> simple time
    parameter MAX_COUNT     =       3        ,
    parameter COUNT_BITS    =       12
)(
    .          input           i_clk                   ,
    .input           i_rst_n                 ,
  .  input  [7      :0        ]    i_tx_data               ,
  .  input           i_tx_data_valid         ,
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

vcode_line = vcode.split("\n")
for line in vcode_line :
    line = remove_more_space(line)
    print(line)


