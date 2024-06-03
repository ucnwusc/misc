import pkgutil
import site
import os
import sys

def find_module_path(module_name):
    for path in site.getsitepackages():
        if pkgutil.find_loader(module_name):
            module = pkgutil.find_loader(module_name).load_module(module_name)
            return os.path.dirname(module.__file__)
    return None

module_name=''
if len(sys.argv) >=2:
    module_name=sys.argv[1]
else:
    module_name = 'rdkit' 
path = find_module_path(module_name)

if path:
    print(f"{module_name} is installed in: {path}")
else:
    print(f"{module_name} is not found in standard site-packages directories.")
