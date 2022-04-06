from zipfile import ZipFile


def unzip(file: str, path: str):
    with ZipFile(file, 'r') as zip:
        zip.extractall(path)