import os


# create test for mkdirs


def mkdirs(base_path: str, dirs: []):
    for directory in dirs:
        os.makedirs(f"{base_path}/{directory}")


def touch(base_dpath: str, files: []):
    for filename in files:
        open(f"{base_dpath}/{filename}", 'a').close()


def render_template(template_path, output_directory, search_replace: []):
    for search, replace in search_replace:
        with open(template_path, 'r') as file:
            filedata = file.read()

        filename = os.path.basename(template_path)

        updated_content = filedata.replace(search, replace)

        with open(output_directory + "/" + filename, 'w') as file:
            file.write(updated_content)
