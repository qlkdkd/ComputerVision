import os

root = './transformed/c4/'

def makeForder():
    if not os.path.exists(root):
        os.makedirs(root)
    else: print('경로 이미 존재')

if __name__ == '__main__':
    makeForder()