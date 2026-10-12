import os


def csv_split(path:str,output_path:str,out1:str,out2:str):
    
    file = open(path, "r")
    os.makedirs(output_path, exist_ok=True)
    f1 = open(output_path + out1, "w")
    f2 = open(output_path + out2, "w") #Use w so it creates a new fresh file else it will create an infinite append
  
    for line in file:
        first = line.find(",")
        second = line.find(",",first + 1)
        c1 = line[:second]
        c2 = line[second + 1:]
        f1.write(c1 +'\n') #No indent if we don't add the newline character
        f2.write(c2)
    print("hello")
    file.close()
    f1.close()
    f2.close()


csv_split("data/DataTestInput.csv", "data/split/", "Dry.txt", "TIM.txt")

        