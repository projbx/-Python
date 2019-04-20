import os

def createdir(dirname):
    dir_path = os.path.join(os.getcwd(), dirname)
    try:
        os.mkdir(dir_path)
        return 0
    except FileExistsError:
        return 1

def deldir(dirname):
    dir_path = os.path.join(os.getcwd(), dirname)
    try:
        os.rmdir(dir_path)
        return 0
    except OSError:
        return 1

def changedir(dirname):
    dir_path = os.path.join(os.getcwd(), dirname)
    try:
        os.chdir(dir_path)
        return 0
    except FileExistsError:
        return 1

def listdir():
    return os.listdir(path=os.getcwd())

if __name__ == "__main__":
    
    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.
    for i in range(9):
        newdir = 'dir_%s' % (i+1,)
        createdir(newdir)

    for i in range(9):
        deldir = 'dir_%s' % (i+1,)
        createdir(newdir)

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.
    print(listdir())

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    orig_fname = os.path.basename(__file__)
    copy_fname = orig_fname + '_copy'
    os.popen('copy %s %s' % (orig_fname,copy_fname))

    
