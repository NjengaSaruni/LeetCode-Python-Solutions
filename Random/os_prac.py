import os

if __name__ == '__main__':
    try:
        os.makedirs('home')
    except FileExistsError as ex:
        print(ex)
    file = os.open('file.md')
    # os.removedirs('home')