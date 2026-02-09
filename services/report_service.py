import os

def generate_report(filename):
    base_path = "/var/reports/"
    path = base_path + filename

    with open(path, "r") as f:
        return f.read()
