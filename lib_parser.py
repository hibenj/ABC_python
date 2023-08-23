def parse_file():
    with open('/home/benjamin/Documents/Repositories/cda-tum/cryogenic-cmos/standard_cell_libraries/0.7V_10K.lib', 'r') as reader:

        # indicate which struct is viewed
        p_cell = False
        p_pin = False
        p_internal = False
        p_fall = False
        p_values = False

        # counters
        cell_counter = 0
        pin_counter = 0
        bracket_counter = 1
        
        # structs
        cells = {}
        input_pins = []
        output_pins = []
        name_cell = ''
        name_pin = ''
        
        for line in reader:
            line = line.lstrip()
            if not line:
                continue

            if line.startswith("cell("):
                p_cell = True
                cell = {}
                cell_counter += 1
                bracket_counter = 0

                start_index = len("cell(")
                end_index = line.find(")")
                if end_index != -1:
                    name_cell = line[start_index:end_index]

            if "pin(" in line:
                p_pin = True
                pin = []
                power_entries = []
                start_index = len("pin(")
                end_index = line.find(")")
        
                if end_index != -1:
                    name_pin = line[start_index:end_index]

            if "internal_power" in line and p_pin == True:
                p_internal = True
            
            if "fall_power" in line and p_pin == True:
                p_fall = True
            
            if p_values == True and ";" in line:
                vl.append(float(line.split("\"")[0]))
                values = (vl)

            if "values" in line and p_pin == True and p_internal == True:
                if p_fall == True:
                    values = []
                p_values = True
                vl_line = ''
                if ";" in line:
                    vl_line = line.split("(\"")[1].split("\")")[0]
                else:
                    vl_line = line.split("\"")[1].split(", \\")[0]
                vl = [float(num.replace('"', '')) for num in vl_line.split(",")]
                if ";" in line:
                    values = (vl)

            if "{" in line:
                bracket_counter += 1
            
            if "}" in line:
                bracket_counter -= 1

            if bracket_counter == 3 and p_values == True:
                pin.append(values)
                p_values = False

            if bracket_counter == 3 and p_fall == True:
                p_fall = False

            if bracket_counter == 2 and p_internal == True:
                power_entries.append(values)
                p_internal = False
            
            if bracket_counter == 1 and p_pin == True:
                cell[name_pin] = pin
                p_pin = False

            if bracket_counter == 0 and p_cell == True:
                p_cell = False
                cells[name_cell] = cell
            

    return cells

    # print(cells['AND2x2_ASAP7_75t_R'])