# try, catch

try:
    with open('filelog.txt','r') as reader:
        reader.read()


except:
    print("Some how i reached the block because there is failure in try block")

    