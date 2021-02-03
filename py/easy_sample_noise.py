import soundfile as sf
import os
# path:./DNS-Challenge/datasets/noise
# path = os.getcwd()
# filepath= path +'/datasets/noise'

# find the path of wav
filepath = './datasets/noise'
filenames=os.listdir(filepath)
print(len(filenames))

# given parameter
m = 5 #number of samples
ls =[]  # save sample name
counter = 0 # nimber of saved sample 
for filename in filenames:
    if counter < m:
        ls.append(filename)
        counter += 1
#save file
file = open('save_noise.txt','w')
file.write(str(ls))
file.close()
    
    


