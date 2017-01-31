import re

from constants import *

def find_symbols(lines):
    symbols = {};
    labels = {};

    for (line_num,line) in enumerate(lines):
        match1 = re.match(r'@(\D.+)', line);
        match2 = re.match(r'\((.+)\)', line);
        if (match1):
            symbol = match1.group(1);
            if (symbol in SYMBOL_TABLE):
                symbols[symbol] = SYMBOL_TABLE[symbol] 
            elif (symbol not in symbols):
                symbols[symbol] = -1;
        elif (match2):
            label = match2.group(1);
            symbols[label] = line_num - len(labels);
            labels[label] = line_num - len(labels)

    return symbols;

def replace_symbols(lines, symbols):
    output = [];
    current_symbol = START_VARIABLES;

    for line in lines:
        match1 = re.match(r'@(\D.+)', line);
        match2 = re.match(r'\((.+)\)', line);
        if (match1):
            symbol = match1.group(1);
            if (symbols[symbol] == -1):
                output.append('@{}'.format(current_symbol));
                symbols[symbol] = current_symbol;
                current_symbol+=1;
            else:
                output.append('@{}'.format(symbols[symbol]));
        elif (not match2):
            output.append(line);
    return output;

def convert_instructions(lines):
    output = []
    for line in lines:
        line = line.replace(' ','');
        match = re.match(r'@(\d+)', line);
        if (match):
            number = int(match.group(1));
            output.append('{0:016b}'.format(number));
        else:
            instruction = C_INS;
            command = line.split('=');
            if (len(command) > 1):
                left_side = command[0];
                right_side = command[1];
                for dest, value in DEST_TABLE.items():
                    if dest in left_side:
                        instruction |= value << 3;
                instruction |= COMP_TABLE[right_side] << COMP;
            else:
                command = line.split(';');
                instruction |= LABEL_TABLE[command[0]] << COMP;
                if ('L' in command[1]):
                    instruction |= 0b100;
                if ('E' in command[1]):
                    instruction |= 0b010;
                if ('G' in command[1]):
                    instruction |= 0b001;
                if (command[1] == 'JNE'):
                    instruction = (instruction & ~0b111) | 0b101;
                elif (command[1] == 'JMP'):
                    instruction |= 0b111;
            output.append('{0:016b}'.format(instruction));
    return output;

