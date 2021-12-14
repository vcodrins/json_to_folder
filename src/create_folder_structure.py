import os


def create_folder_structure(output_folder: str, json_object: dict):
    """
    Creates the file and folder structure to the output folder
    Anything that already exists will be overwritten

    :param output_folder: str
    :param json_object: dict
    """
    for key in json_object:
        item_path = output_folder + "\\" + key
        if isinstance(json_object[key], dict):
            if not os.path.exists(item_path):
                os.mkdir(item_path)
            create_folder_structure(item_path, json_object[key])
        else:
            if not os.path.exists(item_path):
                open(item_path, "x")
            file = open(item_path, "w")
            file.write(json_object[key])
