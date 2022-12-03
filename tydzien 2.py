# with open("data.txt") as f:
#     lines = f.readlines()
#     f.close()

# with open("data.txt", 'w+') as f:           #argument w - do zapisu w+ do zapisu i odczytu
#     lines = f.readlines()
#     f.close()

# with open("data.txt", 'w+') as f:           #argument w - do zapisu w+ do zapisu i odczytu
#    f.write("test")
#    f.close
   
# with open("data.txt", 'a') as f:           #argument w - do zapisu w+ do zapisu i odczytu
#    f.write("Adam slodowy")
   
#    f.close


# for line in lines:
#     print(line)



# try:
#     with open("adata.txt") as f:
#         lines = f.readline()

# except FileNotFoundError:
#     print("nie ma pliku")
# finally:
#     print("problm ze znalezieniem pliku")
#     # f.close()


list = [1,2,3,4]
strings = ["das", "asdas", "asdad"]
tuple = (234,234 , "dffdf")
sety =  {'apple',  'orange', 'pear'}

#slowniki            #klucz i wartosc
dict_example = dict([("klucz1", "wartossc1"), ("klucz2", "wartosc2"), ("klucz3", "warosc3")])
print(dict_example.keys())
print(dict_example.values())

for k,v in dict_example.items():
    print("Klucz: " + k , "wartosc: " + v)




# intttt = list.count()
# print(intttt)