from lib_parser import parse_file as parse

cells = parse()

cell = cells['AND2x2_ASAP7_75t_R']

def cmp_avg_cell_internal(cell):
    avg_cell_internal = 0
    counter = 0
    for pin in cell.keys():
        #print(pin)
        if pin != 'Y':
            for value_vector in cell[pin]:
                #print(value_vector)
                for value in value_vector:
                    avg_cell_internal += abs(value)
                    counter += 1

    avg_cell_internal /= counter
    print(avg_cell_internal)

def cmp_avg_net_switching(cell):
    avg_net_switching = 0
    counter = 0
    for pin in cell.keys():
        if pin == 'Y':
            for value_vector in cell[pin]:
                for value in value_vector:
                    avg_net_switching += abs(value)
                    counter += 1

    avg_net_switching /= counter
    print(avg_net_switching)

cmp_avg_cell_internal(cell)
cmp_avg_net_switching(cell)


#print(cell)