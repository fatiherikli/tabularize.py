"""
Tabularize module
Contains the `load` and `loads` methods like json, yaml modules.
"""

def normalize_line(line):
    return [piece.strip() for piece in line.split("|")[1:-1]]

def is_valid_line(line):
    return "|" in line

def loads(text, return_type=dict):
    """Loads tabular data from provided string"""
    lines =  map(normalize_line,
                filter(is_valid_line,
                        text.strip().splitlines()))

    keys = lines.pop(0)

    if not issubclass(return_type, dict):
        return map(return_type, lines)

    return [return_type(zip(keys, line)) for line in lines]

def load(source):
    """Reads the tabular data of file-like objects"""
    return loads(source.read())

def from_docstring(_object, *args, **kwargs):
    """Loads the docstring of object as tabular data"""
    return loads(_object.__doc__, *args, **kwargs)
