class my_file_reader():
    def __init__(self, file_path):
        self.path = file_path
        self.file_object = None

    def __enter__(self):
        self.file = open(self.path)
        return self.file

    def __exit__(self, type, val, tb):
        self.file.close()

    # Additional methods implemented below


    # Implement a read() method
    



    # Implement a readlines() method



    # Implent a readline() method



