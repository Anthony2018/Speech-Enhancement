import soundfile as sf
import os
# path:./DNS-Challenge/datasets/clean/read_speech
# path = os.getcwd()
# filepath= path +'/datasets/clean/read_speech'

# find the path of wav
filepath = './datasets/clean/read_speech'
filenames=os.listdir(filepath)
print(len(filenames))

# given parameter
n = 5 #number of samples
dic = {} # save the smaple info in a dictionary (key,value)=(reader:n)
ls =[]  # save sample name
for filename in filenames:
    reader_name = filename.split("_")[5]
    if reader_name in dic:
        if dic[reader_name] < n:
            dic[reader_name] +=1
            ls.append(filename) 
    else:
        dic[reader_name] = 1
        ls.append(filename)

#save file
file = open('save_clean.txt','w')
file.write(str(ls))
file.close()
    
    


