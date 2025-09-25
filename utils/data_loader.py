import json

# fazer com que todas os test que usam a funcao de loeader chamar essa funcao, remover a duplicodade
def load_json_data(path):
    """Loads data from a JSON file."""
    with open(path, 'r') as f:
        return json.load(f)