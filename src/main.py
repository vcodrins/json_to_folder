import json
import os.path
import sys
from exceptions import *
from create_folder_structure import create_folder_structure


def main():
    try:
        if len(sys.argv) != 3:
            raise InvalidArgumentCount
        if not os.path.exists(sys.argv[2]):
            raise InvalidFilePath
        if not os.path.exists(sys.argv[1]):
            raise InvalidFolderPath
        try:
            json_object = json.load(open(sys.argv[2]))
        except ValueError:
            raise InvalidJsonFile
        output_folder = sys.argv[1]
        create_folder_structure(output_folder, json_object)
    except InvalidArgumentCount:
        print("""
            Invalid number of arguments
            Please make sure to use quotes for outputFolder and jsonFile if path includes spaces

            Valid paths may be:
                "file.json"
                "./file.json"
                "folder/file.json"
                "./folder/file.json"
                "absolute/path/to/file.json"

            Usage: 
                main.py "<outputFolder>" "<jsonFile>"
            """)
    except InvalidFolderPath:
        print("""
            Output folder does not exist
        """)
    except InvalidFilePath:
        print("""
            Input json file does not exist
        """)
    except InvalidJsonFile:
        print("""
            Input json file is invalid
        """)


main()
