try:
    with open('test','r') as reader:
        reader.read()

except:
    print("Escaped test case")


try:
    with open('test','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Clean up records")