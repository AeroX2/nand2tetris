import os;

def open_file(file_name):
    try:
        if (os.path.splitext(file_name)[1] == '.asm'):
            return open(file_name, 'r');
        else:
            print('Ignoring file, {} does not have a .asm extension'.format(file_name))
    except:
        print('Could not open file');
        print('Usage: assembler.py file');
    return None;

def read_strip_file(f):
    lines = []
    for line in f.readlines():
        line = line.strip();
        if (line and not line.startswith('//')):
            line = line.split('//')[0].strip();
            lines.append(line);
    return lines

def write_file(f, lines):
    dir_path = os.path.dirname(f.name);
    file_name = os.path.basename(f.name).split('.')[0]
    path = os.path.join(dir_path, file_name+'.hack');
    wf = open(path, 'w');
    wf.write('\n'.join(lines));
    return path;

