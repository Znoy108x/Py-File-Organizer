# This file contains code for organising files in a directory :D
import os
# All possible file extensions
ImageFileExtensions = [".jpg", ".jpeg", ".png", ".gif",
                       ".bmp", ".tiff", ".tif", ".psd", ".svg", ".eps"]
AudioFileExtensions = [".mp3", ".wav", ".aac", ".flac", ".ogg"]
VideoFileExtensions = [".mp4", ".avi", ".mov", ".wmv", ".mkv"]
TextFileExtensions = [".txt", ".csv", ".xml", ".json"]
DocumentsFileExtensions = [".doc", ".docx", ".pdf",
                           ".ppt", ".pptx", ".xls", ".xlsx", ".odt"]
ArchieveFileExtensions = [".zip", ".rar", ".7z", ".tar"]
ExecutableFileExtensions = [".exe", ".dmg",
                            ".apk", ".bat", ".bin", ".jar", ".wsf"]
DatabaseFileExtensions = [".sql", ".mdb", ".sqlite", ".db"]
FontFileExtensions = [".ttf", ".otf", ".woff", ".woff2"]
WebFileExtensions = [".html", ".css", ".js", ".php", ".xhtml", ".asp", ".aspx",
                     ".cer", ".cfm", ".cgi", ".pl", ".xpl", ".xql", ".xsd", ".xslt", ".yaml", ".yml"]
# Checking if there is a folder with FoldeName in this directory
def Create_Folder(FolderName):
    if not os.path.exists(FolderName):
        os.makedirs(FolderName)
# Getting all the files present in the directory where this pyhton file is present
All_Files_In_This_Directory = os.listdir()
All_Files_In_This_Directory.remove("FileOrganiserCode.py")
print("All Files", All_Files_In_This_Directory)
# Grouping all the files with same class
Image_Files = []
Audio_Files = []
Video_Files = []
Text_Files = []
Document_Files = []
Archieve_Files = []
Executable_Files = []
Database_Files = []
Font_Files = []
Web_Files = []
# Checking if there is need for creating the folder.
def Check_Image_Files():
    global Image_Files
    Image_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in ImageFileExtensions]
    if (len(Image_Files) > 0):
        Create_Folder("Images")
# Checking if there is need for creating the folder.
def Check_Audio_Files():
    global Audio_Files
    Audio_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in AudioFileExtensions]
    if (len(Audio_Files) > 0):
        Create_Folder("Audio")
# Checking if there is need for creating the folder.
def Check_Video_Files():
    global Video_Files
    Video_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in VideoFileExtensions]
    if (len(Video_Files) > 0):
        Create_Folder("Video")
# Checking if there is need for creating the folder.
def Check_Text_Files():
    global Text_Files
    Text_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in TextFileExtensions]
    if (len(Text_Files) > 0):
        Create_Folder("Text")
# Checking if there is need for creating the folder.
def Check_Document_Files():
    global Document_Files
    Document_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in DocumentsFileExtensions]
    if (len(Document_Files) > 0):
        Create_Folder("Document")
# Checking if there is need for creating the folder.
def Check_Archieve_Files():
    global Archieve_Files
    Archieve_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in ArchieveFileExtensions]
    if (len(Archieve_Files) > 0):
        Create_Folder("Archieve")
# Checking if there is need for creating the folder.
def Check_Executable_Files():
    global Executable_Files
    Executable_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in ExecutableFileExtensions]
    if (len(Executable_Files) > 0):
        Create_Folder("Executable")
# Checking if there is need for creating the folder.
def Check_Database_Files():
    global Database_Files
    Database_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in DatabaseFileExtensions]
    if (len(Database_Files) > 0):
        Create_Folder("Database")
# Checking if there is need for creating the folder.
def Check_Font_Files():
    global Font_Files
    Font_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in FontFileExtensions]
    if (len(Font_Files) > 0):
        Create_Folder("Font")
# Checking if there is need for creating the folder.
def Check_Web_Files():
    global Web_Files
    Web_Files = [File_Info for File_Info in All_Files_In_This_Directory if os.path.splitext(
        File_Info)[1].lower() in WebFileExtensions]
    if (len(Web_Files) > 0):
        Create_Folder("Web")
# Generating Folders
Check_Image_Files()
Check_Audio_Files()
Check_Video_Files()
Check_Text_Files()
Check_Document_Files()
Check_Archieve_Files()
Check_Executable_Files()
Check_Database_Files()
Check_Font_Files()
Check_Web_Files()

print(Image_Files)
print(Audio_Files)
print(Video_Files)
print(Text_Files)
print(Document_Files)
print(Archieve_Files)
print(Executable_Files)
print(Database_Files)
print(Font_Files)
print(Web_Files)
# Moving the files in their respectice category filders
def Reallocater(Folder_Name, File):
    os.replace(File, f"{Folder_Name}/{File}")
def FilesLooper(FilesList, FolderName):
    for File in FilesList:
        Reallocater(FolderName, File)
FilesLooper(Image_Files , "Images")
FilesLooper(Video_Files , "Video")
FilesLooper(Text_Files , "Text")
FilesLooper(Document_Files , "Document")
FilesLooper(Archieve_Files , "Archieve")
FilesLooper(Executable_Files , "Executable")
FilesLooper(Database_Files , "Database")
FilesLooper(Font_Files , "Font")
FilesLooper(Web_Files , "Web")