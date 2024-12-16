# Adding the lists of colors is a json to get them later
def add_list_json(element, content) : 
    import json
    from src.helpers import eprint

    try : 
        with open("json/palettes.json", 'r') as f : 
            data = json.load(f)
        data[element] = content
        with open("json/palettes.json", 'w') as f:
            json.dump(data, f)
            
    except FileNotFoundError : 
        eprint("Error! File 'json/palettes.json' was not found!")