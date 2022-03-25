print("hello")
a=3
print(a)
Str = "Hello World"
print(Str)
b, c, d = 5,6.4,"Great"
#to concatinate two different datatype
print("{} {}".format("Value is",b))
#to know what kind of variable
print(type(b))
#List is data type that allows multiple values and can be different data types
values = [1, 2, "Saherul", 4, 5]
print(values[0])
print(values[3])
#Extract last index
print(values[-1])
#Extract sub index
print(values[1:4])
#Insert the values in the list
values.insert(3,"james")
values.append("End")
print(values)
#Update the value
values[2]="SAHERUL"
print(values)
#Delete the value
del values[0]
print(values)
#Tuple - Same as LIST Data type but immutable
values = (1, 2, "VOKJ", 4.5)
print(values[2])
#values[2] = "JJJ"
print(values)
#Dictionary (key,pair values), In JAVA we call as HashMap
dic={"a":2, 4:"bcd", "c":"Hello World"}
print(dic["c"])
#Another way of doing the Dictionary
dict={}
dict["firstname"] = "dinesh"
dict["lastname"] = "krishna"
print(dict)
print(dict["lastname"])


