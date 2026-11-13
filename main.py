from pathlib import Path
import argparse
from emojis import emojis



'''
    Idea 

    python tree.py --input <Path> 


    python tree.py --input .

    py-tree
        documents
            reports.pdf
            invoice/
                invoices.pdf

    
                
    



'''


def registerArgs():
    parser = argparse.ArgumentParser(description="Welcome to Njabs File tree Managements")
    parser.add_argument("-i", "--input", help="The file you want to see the tree")
    parser.add_argument("-o", "--output", help="Output file ")
    parser.add_argument("-n", "--name", help="Name of the project")
    args = parser.parse_args()
    return None if not args else args

def main(args : argparse.Namespace) -> dict: 
    tree = {}
    path = Path(args.input) if args.input  else Path.cwd()

    if not path.exists():
        print(f"{args.input} <- this path is not existing Please type existing path")
        return
    if path.is_file():
        path = Path(path.parent)

    tree["ProjectName"] = path.absolute().name
    if args:
        if args.name:
            tree['ProjectName'] = args.name

    currentDirFiles = getFiles(path=path)
    folders = getFolders(path=path)

    if currentDirFiles : tree["currentDIRFiles"] = currentDirFiles
    results : list[tuple[int, Path]] = compute(folders)
    tree["everything"] = results
    return tree


def standarlize(paths: dict) -> None : 
    print(paths)
    spaces = 2

    print(f"{emojis["folder"]} {paths["ProjectName"]}/")
    if "currentDIRFiles" in paths:  
        for file in paths["currentDIRFiles"]:
            p = Path(file)
            emote = str(p.suffix).replace(".", "")
            if emote in emojis: print(f"{" "*spaces} {emojis[emote]} {file}")
            else: print(f"{" "*spaces} {emojis[emote]} {file}")


    
    
    

    
def compute(listFolders : list[Path]) -> list[tuple[int, str]]:
    formatted: list[tuple[int, Path]] = []
    for i, p in enumerate(listFolders, start=1):
        formatted.append((i,p))
    FolderFiles = []
    savePath = []
    start = 0
    while (len(formatted) != 0 ):
        currentFiles = []
        currentFolders = []
        if formatted[start][-1].is_dir():
            savePath.append(formatted[start])
            FolderFiles.append(formatted[start])
            if formatted[start][0] > 10:
                currentFiles.extend([(formatted[start][0]* 10 + i, p) for i, p in enumerate(getFiles(formatted[start][-1]), start=1)])
            else: currentFiles.extend([(formatted[start][0] , i) for i in getFiles(formatted[start][-1])])
            currentFolders.extend([(formatted[start][0]* 10 + i, p) for i, p in enumerate(getFolders(formatted[start][-1]), start=1)])
            if currentFiles: FolderFiles.extend(currentFiles)
            if currentFolders :
                formatted.extend(currentFolders)
            formatted.pop(0)
    return FolderFiles

        



    








def filesNames(pathList: list[Path]) -> list[str]:
    return [file.name for file in pathList]


def getFiles(path: Path) -> list[Path]:
    return [i.name for i in path.iterdir() if i.is_file() and i.name != ".git"]

def getFolders(path: Path) -> list[Path]:
    return [i for i in path.iterdir() if i.is_dir() and i.name != ".git"]

    



'''
    What I can do is to encrypt the folders  and they will represent the structure
    Second Idea I have decided to go with
    tree  = {
        ProjectName : <NAME>,
        currentDIRFiles: [*<FILE NAMES>],
        everything: [folder1, app.py1, njabs.pdf1, folder2, index.xml2, folder3 ]
    }
    
    
    First IDEA
    1tree = {
        ProjectName : <NAME>,
        currentDIRFiles: [*<FILE NAMES>],
        everything: [
                {FolderName: <NAME>, files: [<FILE NAMES>], FOLDERS: [Folders]},
                {},
                {}
        
        ]
    
    }

'''





if __name__ == "__main__":
    d = main(registerArgs())
    standarlize(d)

