from pathlib import Path
import json
def get_model_data (filename:str)->dict :
    """
    Loads model configuration from a JSON file.
    Args:
        filename (str): The name of the JSON file to load.
    Returns:
        dict: The loaded data as a dictionary.
        None: If the file is missing, corrupted, or inaccessible.
    """
    file_path = Path(__file__).parent/filename
    try : 
        if file_path.is_file(): 
            with open(file_path, 'r', encoding='utf-8') as r :
                data = json.load(r)
                return data
    except (json.JSONDecodeError) as e:
        print(f"Syntax Error in {filename}: {e}")
        return None
    except (Exception) as e : 
        print(f"Unexpected Error: {e}")
        return None
