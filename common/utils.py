def read_file(file_path):
    with open(file_path, 'r') as f:
        return [x.strip() for x in f.readlines()]
