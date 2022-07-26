import json


def persist_output(json_string, target_path) -> None:
    '''
    Opening a target path of a string and then converting it to a JSON object
    Variable i gives that in the terminal each JSON object is followed
    by a new line character if JSON object is valid and i is bigger than 1
    :param json_string: String
    :param target_path: String
    :return: None
    '''
    i = 0
    with open(target_path, 'a') as outfile:
        if i == 0:
            json.dump(json_string, outfile)
            outfile.write('\n')
            i += 1
        else:
            json.dump(json_string, outfile)
            outfile.write('\n')
