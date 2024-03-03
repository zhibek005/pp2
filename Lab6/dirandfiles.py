#1
import os

p = '/your/specified/path' 
d = [d for d in os.listdir(p) if os.path.isdir(os.path.join(p, d))]
f = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
a = os.listdir(p)

print("Directories:", d)
print("Files:", f)
print("All:", a)

#2
p = '/your/specified/path' 

e = os.path.exists(p)
r = os.access(p, os.R_OK)
w = os.access(p, os.W_OK)
x = os.access(p, os.X_OK)

print("Exists:", e, "Readable:", r, "Writable:", w, "Executable:", x)

#3
p = '/your/specified/path/file.txt' 
e = os.path.exists(p)

if e:
    f = os.path.basename(p)
    d = os.path.dirname(p)
    print("Filename:", f, "Directory:", d)
else:
    print("Path does not exist.")

#4
with open('/path/to/your/file.txt', 'r') as file: 
    l = sum(1 for _ in file)
    print("Number of lines:", l)

#5
l = ['line 1', 'line 2', 'line 3']  

with open('/path/to/your/file.txt', 'w') as file: 
    for item in l:
        file.write("%s\n" % item)

#6
import string

for c in string.ascii_uppercase:
    with open(f"{c}.txt", 'w') as file:
        pass  

#7
import shutil

shutil.copyfile('/path/to/source/file.txt', '/path/to/destination/file.txt') 

#8
p = '/path/to/your/file.txt'  

if os.path.exists(p) and os.access(p, os.W_OK):
    os.remove(p)
    print("File deleted.")
else:
    print("File does not exist or is not writable.")
