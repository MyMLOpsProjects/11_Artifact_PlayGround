def createfile(name):
    with open(name, 'w') as f:
        f.write("This is a file created by createfile function.\n")

        
createfile("demo.txt")        