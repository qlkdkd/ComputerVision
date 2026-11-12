import os

def makeForder():
    if not os.path.exists('./transformed/c3'):
        os.makedirs('./transformed/c3')

makeForder()