import os
import json

def readFiles(dir):
    file_dict = {}
    for filename in os.listdir(dir):
        if filename.endswith(".json"):  
            json_path = os.path.join(dir, filename)
            with open(json_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    file_dict[item.get("filename")] = item.get("code")
    return file_dict

def writeFeedback(dir, file_name, feedback):
    feedback_file = file_name[:-3] + "_feedback" + ".txt"
    path = os.path.join(dir, feedback_file)
    with open (path, 'w') as file:
        file.write(feedback)