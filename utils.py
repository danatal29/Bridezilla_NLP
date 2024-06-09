import pickle
from typing import Union, List, Dict


def save_pickle(file_path: str, obj: Union[List, Dict]):
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)

def load_pickle(file_path: str):
    with open(file_path, 'rb') as file:
        loaded_file = pickle.load(file)
    return loaded_file
