# [] create The Weather
# [] edX assignment page
import os
cmd = "curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt"
returned_ = os.system(cmd)
          
#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt 

mean_file = open("mean_temp.txt", "a+")
line_To_Be_Added = 'Rio de Janeiro,Brazil,30.0,18.0\n'
mean_file.write(line_To_Be_Added)          
mean_file.seek(0)                    
headings = mean_file.readline()     
headings = headings.split(',')  

while True:
    city_temp = mean_file.readline()
    if not city_temp:
        break
    city_temp = city_temp.split(',')
    print(headings[0],'of',city_temp[0],headings[2],'is',city_temp[2],'Celsius')
    
mean_file.close()