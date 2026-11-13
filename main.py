from pathlib import Path
import argparse
from emojis import emojis
import colorama
from colorama import Fore, Back, Style
import re

colorama.init(autoreset=True)

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

    print(path.absolute())

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

    if args.output: return tree, args.output
    return tree

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
    return [i.name for i in path.iterdir() if i.is_file() and i.name != ".git" and i.name != "__pycache__" and i.name != ".venv"]

def getFolders(path: Path) -> list[Path]:
    return [i for i in path.iterdir() if i.is_dir() and i.name != ".git" and i.name != "__pycache__" and i.name != ".venv"]

def standarlize(paths: dict, output_file: str = None) -> None : 
    # print(paths)
    ANSI_PATTERN = re.compile(r"\x1b\[[0-9;]*m")

    spaces = 2
    tree_lines = []

    def emit(line: str) -> None:
        print(line + Style.RESET_ALL) 
        tree_lines.append(ANSI_PATTERN.sub("", line)) 


    if "ProjectName" in paths: emit(f"{emojis.get('folder', '📁')} {paths['ProjectName']}/")

    if "currentDIRFiles" in paths:
        for file in paths["currentDIRFiles"]:
            p = Path(file)
            emote = str(p.suffix).replace(".", "")
            file_emoji = emojis.get(emote, emojis.get("file", "📄"))
            emit(f"{' ' * spaces}{file_emoji} {Fore.GREEN + file}")
            
        if "everything" in paths:
            everything = sorted(paths["everything"], key=lambda x: str(x[0]))
            folder_ids = {item_id for item_id, item in everything if isinstance(item, Path) and item.is_dir()}

            for item_id, path_item in everything:
                id_str = str(item_id)
                level = len(id_str)
                p = Path(path_item) if isinstance(path_item, str) else path_item
                name = p.name if isinstance(path_item, Path) else path_item
                is_folder = isinstance(path_item, Path) and path_item.is_dir()

                if is_folder:
                    folder_emote = emojis.get("folder", "📁")
                    emit(f"{' ' * (spaces * level)}{folder_emote} {Fore.BLUE + name}/")
                else:
                    # A file sharing its ID with a folder lives INSIDE that folder
                    if item_id in folder_ids:
                        level += 1

                    emote_key = str(p.suffix).replace(".", "") if isinstance(p, Path) else ""
                    file_emoji = emojis.get(emote_key, emojis.get("file", "📄"))
                    emit(f"{' ' * (spaces * level)}{file_emoji} {Fore.GREEN+name}")

    if output_file != None and output_file.endswith(".txt"):
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(tree_lines) + "\n")
        print(f"\nSaved to {output_file}")


    print(f"Successfully presented the tree to your Project {paths['ProjectName']}")


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
    if isinstance(d, tuple): standarlize(d[0],d[-1])
    else: standarlize(d)

