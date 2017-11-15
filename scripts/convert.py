import os
from shutil import copyfile

def convert(source, dest):
    os.system('python ./lib/xlsx2csv/xlsx2csv.py "{}" \"{}\" -d \'tab\''.format(source, dest))
#    os.system('aspell check {}'.format(dest))
    
def copy(source, dest):
    #os.system('cp "{}" "{}"').format(source, dest)
    try:
        os.makedirs('./test/' + number)
    except Exception:
        print 'already exists'
    copyfile(source, dest)

sources = os.listdir("./in")

for source in sources:
    if '.' in source: continue
    number = source.split(' ')[0]
    source = "./in/" + source
    files = os.listdir(source)
    try:
        os.makedirs('./test/' + number)
    except Exception:
        print 'already exists'
    for file in files:
        if '.xlsx' not in file:
            sourcefile = source + '/' + file
            dest = './temp/' + number + '/' + file
            copy(sourcefile, dest)
            continue
            
        filename = 'x'
        if file.startswith('s') or file.startswith('S'):
            filename = 's'
        elif file.startswith('b') or file.startswith('B'):
            filename = 'b'
        elif file.startswith('h') or file.startswith('H'):
            filename = 'h'
        filename = filename + '.csv'
        sourcefile = source + '/' + file
        dest = './temp/' + number + '/' + filename
        
        convert(sourcefile, dest)
