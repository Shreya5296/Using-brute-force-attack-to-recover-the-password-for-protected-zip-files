import zipfile                     #Library used for password encrypted zipped folder/file
import time

folderpath = input('Path to the file: ')  #Get the target file path and name from the user
folderpath = folderpath.strip()
zipf = zipfile.ZipFile(folderpath)      #Initialize a PdfFileReader object                             

if not zipf:           #Checks if the file is password encrypted
    print('The zipped file/folder is not password protected! You can successfully open it!')  #Notifies if the zipped file/folder is not password encrypted

else:
    starttime = time.time()             #Save the start time
    result = 0                          #Intialize a variable result with zero. '0' will indicate Failure, while '1' will idicate Success
    c = 0                               #Initialize a variable c to keep the count of passwords tried

    #Build a character array including all numbers,lowercase letter, uppercase letters and special haracters. Total 10+26+26+33 = 95 characters
    characters =['0','1','2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z',
                 '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']

    
    print("Brute Force Started...")
    
    #If still the password is not found i.e. result = 0, the below loop will try four character passwords. 81450625 Possible Combinations        
    if(result == 0):
        print("Checking for 4 character password...")
        for i in characters:
            for j in characters:
                for k in characters:
                    for l in characters:
                        guess = str(i) + str(j) + str(k) + str(l)
                        password=guess.encode('utf8').strip()
                        #print(guess)
                        c=c+1
                        try:
                            with zipfile.ZipFile(folderpath,'r') as zf:
                                zf.extractall(pwd=password)
                                print("Success! The password is: "+ guess)
                                endtime = time.time()            #Save the end time
                                result = 1                       #Set result variable to 1 on success
                                break                            #If the password is found break from i for loop
                        except:
                            pass
                    if result == 1:
                        break                           #If the password is found break from j for loop
                if result == 1:
                    break                               #If the password is found break from k for loop
            if result == 1:
                break                                   #If the password is found break from l for loop

    #Finally, if the password is not found even after appying all possile combination of characters upto 4 character length, notify the user as below, else print congratulations
    if(result == 0):
        print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters.")
    else:
        duration = endtime - starttime
        print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')
