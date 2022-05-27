import os

os.chdir('D:/POCRA_Mumbai')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)

    f_title, f_course, f_nam = f_name.split('-')

    #print(f_nam)

    #print('{}{}'.format(f_nam, f_ext))


    f_title = f_title.strip()
    f_course = f_course.strip()
    f_nam = f_nam.strip()


    newName = '{}{}'.format(f_nam, f_ext)

    print(newName)

    os.rename(f, newName)


