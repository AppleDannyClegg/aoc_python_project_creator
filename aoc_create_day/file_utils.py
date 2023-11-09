import os
import shutil


def mkdirs(base_path: str, dirs: []):
    for directory in dirs:
        os.makedirs(f"{base_path}/{directory}")


def touch(base_dpath: str, files: []):
    for filename in files:
        open(f"{base_dpath}/{filename}", 'a').close()


def render_template(template_path, output_directory, search_replace: []):
    current_path = os.path.dirname(__file__)
    template_path = current_path + template_path
    output_directory = os.path.join(os.path.dirname(__file__), output_directory)

    if len(search_replace) == 0:
        shutil.copy(template_path, output_directory)
    else:
        for search, replace in search_replace:
            with open(template_path, 'r') as file:
                filedata = file.read()

            if os.path.isdir(output_directory):
                filename = os.path.basename(template_path)
                output_path = output_directory + "/" + filename
            else:
                output_path = os.path.join(os.path.dirname(__file__), output_directory)

            updated_content = filedata.replace(search, replace)

            with open(output_path, 'w') as file:
                file.write(updated_content)
