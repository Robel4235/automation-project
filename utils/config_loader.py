import yaml

def load_config(path=r'C:\Users\avrah\PycharmProjects1\PythonProject\Api_ui_practice\config\config.yaml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)
