#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    module_name = "hidden_4"
    
    spec = importlib.util.spec_from_file_location(module_name, "path/to/hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    names = [name for name in dir(module) if not name.startswith("__")]
    sorted_names = sorted(names)
    
    for name in sorted_names:
        print(name)
