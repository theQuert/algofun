def pickle_load(path, compression=False):
    if compression:
        with zipfile.ZipFile(path, 'r', compression=zipfile.
