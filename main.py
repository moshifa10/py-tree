from pathlib import Path


def createFilesFolder(*args):

    for pth in args:
        p = Path(pth)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.touch(exist_ok=True)
    print("Successfully created")


file =  Path("documents/report.pdf")

# print(file.name)
# print(file.suffix)
# print(file.stem)
# print(file.parent)
# print(file.absolute())

'''

Activity 2: Check filesystem existence
Difficulty: Easy


Write a program that checks whether the following paths exist:
- documents/
- documents/report.pdf
- documents/missing.pdf
For each path, print whether it exists and whether it is a file or directory.

'''


file2 = Path("documents/")

file3 = Path("documents/missing.pdf")
file4 = Path("documents/report.pdf")

# print(file2.exists())
# print(file3.exists())
# print(file4.exists())
# print(file2.is_file(), file2.is_dir())
# print(file3.is_file(), file3.is_dir())
# print(file4.is_file(), file4.is_dir())



'''

Activity 3: List directory contents
Difficulty: Easy


Write a program that lists everything inside pathlib-practice/.
'''


curr = Path.cwd()
save = [j for i in curr.iterdir() if i.name == "documents" for j in i.iterdir()]

print(save)
'''Activity 4: Find files by extension
Difficulty: Intermediate


Find all PDF files inside the documents/ directory.

Then:
1. Find all .py files inside projects/.
2. Find all .jpg files inside images/.
3. Count how many PDF files exist.'''

globsPDF = [i.glob("*.pdf", case_sensitive=False) for i in curr.iterdir() if i.name == "documents" ]
print("\n\n\nPDF")
for idx, i in enumerate(globsPDF, start=1):
    print(f"{idx}. {list(i)[0].name}")
print(f"Length of the pdf files in documents folder: {len(globsPDF)}" )


globsJPG = [i.glob("*.jpg", case_sensitive=False) for i in curr.iterdir() if i.name == "images" ]

print("\n\n\nJPG")
for idx, i in enumerate(globsJPG, start=1):
    print(f"{idx}. {list(i)[0].name}")

print(f"Length of jpg: {len(globsJPG)}")


globsPY = [j.glob("*.py", case_sensitive=False) for i in curr.iterdir() if i.name == "projects" for j in i.iterdir() ]

print("\n\n\nPYTHON")
print()
for idx, i in enumerate(globsPY, start=1):
    print(f"{idx}. {list(i)[0].name}")

print(f"Length of py files: {len(globsPY)}")



'''Activity 5: Recursive file discovery
Difficulty: Intermediate


Find every file inside pathlib-practice/, including files in nested directories.

Expected output:'''


files = [i for i in Path(".").iterdir() if i.is_file() and i.name != ".git"]
folders = [i for i in Path(".").iterdir() if i.is_dir() and i.name != ".git"]
print(folders)
print(files)



start = 0
while len(folders) != 0:
    if (folders[start].is_dir()):
        curr_folders = [i for i in folders[start].iterdir() if i.is_dir()]
        # print(f"current {curr_folders}")
        if curr_folders : folders.extend(curr_folders)
        curr_file = [i.name for i in folders[start].iterdir() if i.is_file()]
        # print(curr_file)
        if curr_file : files.extend(curr_file)
        folders.pop(0)

# print(files)

for file in files:
    print(file)

def retrieve_all_files(path:Path):
    return [p for p in path.rglob("*.*") if p.is_file() and  ".git" not in p.parts]

# for i in retrieve_all_files(Path(".")):
#     print(i.name)


# new = Path("downloads/documents/example.txt")
# new.parent.mkdir(parents=True, exist_ok=True)
# new.touch(exist_ok=True)


'''

Activity 7: File information
Difficulty: Intermediate


Write a program that retrieves information about every file inside pathlib-practice/.

Display:
- File name.
- Extension.
- File size in bytes.
Example:
report.pdf | .pdf | 2048 bytes
notes.txt  | .txt | 512 bytes
main.py    | .py  | 1024 bytes
'''
listOfAllFiles = retrieve_all_files(Path.cwd())


print("============ Activity 7 ===============")
for f in listOfAllFiles:
    print(f"{f.name}\t|{f.suffix}\t|{f.stat().st_size}")




print("\n\n\n\n")
print("==================== File Explorer =====================")
print("-"*100)


def file_explorer(path: Path):

    directories = 0
    files = 0
    entries = 0
    

    print(f"Directory {path}" )

    filesCount = [i for i in path.iterdir() if i.is_file() and i.name != ".git"]
    folders = [i for i in path.iterdir() if i.is_dir() and i.name != ".git"]


    entries += (len(folders) + len(filesCount))
    if filesCount : files+= len(filesCount)
    if folders : directories+= len(folders)



    start = 0
    while len(folders) != 0:
        if (folders[start].is_dir()):
            curr_folders = [i for i in folders[start].iterdir() if i.is_dir()]
            if curr_folders : folders.extend(curr_folders)
            curr_file = [i.name for i in folders[start].iterdir() if i.is_file()]
            if curr_file : filesCount.extend(curr_file)
            directories += len(curr_folders)
            files += len(curr_file)
            folders.pop(0) 


    print(f"Directories: {directories}")
    print(f"Files: {files}")
    print(f"Entries: {entries}")

file_explorer(Path.cwd())





    



 

# if __name__ == '__main__':
#     createFilesFolder("documents/report.pdf", "documents/notes.txt", "documents/notes.txt", "images/profile.png", "images/logo.jpg", "projects/project1/main.py", "projects/project2/app.py")