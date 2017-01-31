#!/bin/env python3
import sys;

import file_helper;
import lexo_helper;

def main():
    for file_name in sys.argv[1:]:
        f = file_helper.open_file(file_name);
        if (f):
            lines   = file_helper.read_strip_file(f)
            symbols = lexo_helper.find_symbols(lines);
            lines   = lexo_helper.replace_symbols(lines, symbols);
            binary  = lexo_helper.convert_instructions(lines);
            path    = file_helper.write_file(f, binary);

            print('Program compiled and writen to', path);
            for i in range(min(len(lines), 20)):
                print('{:8} {}'.format(lines[i], binary[i]));
            if (len(lines) > 10):
                print('....');
            #import pdb;
            #pdb.set_trace();

if __name__ == '__main__':
    main();
