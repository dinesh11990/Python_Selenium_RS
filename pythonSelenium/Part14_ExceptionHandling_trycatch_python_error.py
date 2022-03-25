# try, catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

#except is like catch in python

except Exception as e:
    print(e)

