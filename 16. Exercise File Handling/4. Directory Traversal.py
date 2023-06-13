import os

def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            ext = filename.split(".")[-1]

            if ext not in extensions:
                extensions[ext] = []

            extensions[ext].append(filename)

        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


directory = input()
extensions = {}  # {py: [example.py, example2.py..], ...}
result = []

try:
    save_extensions(directory)
except FileNotFoundError:
    print(f"Not a valid directory")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")
    [result.append(f"- - - {file}") for file in sorted(files)]

with open("./report.txt", "w") as report_file:
    report_file.write("\n".join(result))