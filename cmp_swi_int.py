from lib_parser import parse_file as parse

cells = parse()

cell = cells['AND2x2_ASAP7_75t_R']

for key in cell.keys():
    print(cell[key])

#print(cell)