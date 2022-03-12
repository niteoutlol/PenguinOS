import os

def command():
    # print(os.listdir(dir))
    files = os.listdir(dir)
    tosend = str('')
    for i in range(len(files)):
        tosend += f'{files[i]}  ' # Make folders blue and files gray / RESET_ALL
    print(tosend)