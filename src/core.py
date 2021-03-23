import src.file as file
import src.constants as k

def convert():
    [file.jsons_to_csv(file_path) for file_path in file.listfiles(k.INPUT_DIR)]
