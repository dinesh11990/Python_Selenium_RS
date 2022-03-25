# try, catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

#except is like catch in python

except Exception as e:
    print(e)

#After try and except, it ll also execute the finally by default
#finally ll be executed even without the except block
#For eg: if there is any data created in try block and at the end of execution finally will clean the data or records


finally:
    print("Cleaning up the records")

