import os
import sys
import fnmatch
import shutil
root = 'c:\\System\\temp\\e\\'
pattern = 'smsm*.235'
outfolder = 'c:\\System\\temp\\'

def line_search(file,output):
    file = open(file,'r')
    output = open(output,'a')
    try:
        for line in file:        
            proc = line[18:30]
            phone = line[37:48]
            date = line[83:85] + '.' + line[81:83] + '.' + line[77:81]
            output.write(proc + '\t' + phone + '\t' + date + '\n')
    except UnicodeDecodeError:
        output.write('UnicodeDecodeError\n')
    output.close()
    file.close()
    


for folder, subdirs, files in os.walk(root):
  print('c',folder)
  for filename in fnmatch.filter(files, pattern):
    fullname = os.path.join(folder, filename)
    print('f',fullname)
    year = folder[17:22]
    #directory = outfolder + year + '\\'
    #os.mkdir(directory)
    #output = os.path.join(outfolder, year + '.txt')
    output = os.path.join(outfolder, 'all4.txt')
    line_search(fullname,output)
    #shutil.copy2(fullname, directory + filename)



    
