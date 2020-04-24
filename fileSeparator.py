import os, shutil


def fileFinder(folderPath, fileExtensions):
    files = []
    for file in os.listdir(folderPath):
        for extension in fileExtensions:
            if file.endswith(extension):
                files.append(file)
    return files


def oneTypeSeparator(folderPath, fileType, fileTuple):
    files = fileFinder(folderPath, fileTuple)
    if len(files) != 0:
        newFolderPath = os.path.join(folderPath, fileType)
        if not os.path.exists(newFolderPath):
            os.mkdir(newFolderPath)
        for item in files:
            itemPath = os.path.join(folderPath, item)
            itemNewPath = os.path.join(newFolderPath, item)
            shutil.move(itemPath, itemNewPath)


def allTypesSeparator(folderPath, dictExtensions):
    for fileType, fileTuple in  dictExtensions.items():
        files = fileFinder(folderPath, fileTuple)
        if len(files) != 0:
            newFolderPath = os.path.join(folderPath, fileType)
            if not os.path.exists(newFolderPath):
                os.mkdir(newFolderPath)
            for item in files:
                itemPath = os.path.join(folderPath, item)
                itemNewPath = os.path.join(newFolderPath, item)
                shutil.move(itemPath, itemNewPath)


def app():
    folderPath = input("Enter folder Path: ")
    if os.path.exists(folderPath):
        print("****MENU****")
        print("Enter yout Choice")
        print("1 => Audio Files")
        print("2 => Video Files")
        print("3 => Images")
        print("4 => Text & Documents")
        print("5 => All Files")
        print("0 => EXIT")

        key = int(input())
        if key == 1:
            oneTypeSeparator(folderPath, 'audios', dictExtensions['audios'])
        elif key == 2:
            oneTypeSeparator(folderPath, 'videos', dictExtensions['videos'])
        elif key == 3:
            oneTypeSeparator(folderPath, 'images', dictExtensions['images'])
        elif key == 4:
            oneTypeSeparator(folderPath, 'texts and documents', dictExtensions['texts and documents'])
        elif key == 5:
            allTypesSeparator(folderPath, dictExtensions)
        elif key == 0:
            print("EXITING")
    
    else:
        print("Path Doesn't Exist")
    print("Thanks for using File Separator")

# EXTENSIONS
dictExtensions = {
    'audios' : ('.mp3', '.m4a', '.wav', '.flac'),
    'videos' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'images' : ('.jpg', '.jpeg', 'png'),
    'texts and documents' : ('.doc', '.pdf', '.txt'),
}

app()