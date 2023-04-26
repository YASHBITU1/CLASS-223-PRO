import zipfile 
import time 

folderpath = input("enter the path to the file")
zipf = zipfile.ZipFile(folderpath)

global result
global tried
result = 0
tried = 0
c=0

if not zipf:
    print("The Zip file is not password protected")
else:
    startTime = time.time()
    wordlistfile = open("wordlist.txt","r",errors="ignore")
    body = wordlistfile.read().lower()
    words = body.split('\n')
    
    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf8').strip()
        c+=1
        print('trying to decode password by {}'.format(word))
        try:
            with zipfile.ZipFile(folderpath,'r') as zf:
                zf.extractall(pwd=password)
                print("Success the password is :"+word)
                endtime = time.time()
                result = 1
            break
        except:
            pass
    if(result == 0):
        print("Sorry password not found")
    else:
        duration = endtime - startTime
        print('password found after trying'+str(c)+' combinations in '+str(duration)+' seconds')
    
    
    
    
    
    