with open('test', 'r') as reader: #if u use this line,  we don't want to use file.close()
    content = reader.readlines()
    reversed(content)
    with open('test', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

