import json
import random

# Acceptible values for 'type' include noun, verb, and adjective.

def get_beginning(type="noun"):
    """_Returns a randomly chosen start of a simple line from the json file_
    
    Defaults to noun content only.

    Returns:
        _str_: _a simple line start string_
    """
    with open(r'content\simple_line_start.json') as source:
        begin_chunk = json.load(source)
    beginnings = begin_chunk[type]
    chosen = random.randint(0, (len(beginnings) - 1))
    beginning = beginnings[chosen]
    return beginning


def get_ending(type="noun"):
    """_Returns a randomly chosen start of a simple line from the json file_
    
    Defaults to noun content only.

    Returns:
        _str_: _a simple line ending string_
    """
    with open(r'content\simple_line_end.json') as source:
        end_chunk = json.load(source)
    endings = end_chunk[type]
    chosen = random.randint(0, (len(endings) - 1))
    ending = endings[chosen]
    return ending


def get_simple(type="noun"):
    """_Combines get_beginning() and get_ending()_

    Returns:
        _str_: _A simple line for a sleep audio_
    """
    beginning = get_beginning(type)
    ending = get_ending(type)
    simple = beginning + " " + ending + "\n"
    return simple


def get_simple_batch(type="noun", size=4):
    """_Returns a stanza of simple lines with the same beginning_

    Args:
        type (str, optional): _Which list the content comes from_. Defaults to "noun".
        size (int, optional): _The size of the batch_. Defaults to 4.

    Returns:
        _str_: _A long string including line breaks with the batch of lines._
    """
    beginning = get_beginning(type)
    endings = []
    result = ""
    for i in range(size):
        endings.append(get_ending(type))
    for ending in endings:
        result = result + beginning + " " + ending + "\n"
    return result
        
    
def print_all_simple(type="noun"):
    """_Prints every combination of simple beginning and ending_
    
    Defaults to noun content only.
    """
    with open(r'content\simple_line_start.json') as start:
        begin_chunk = json.load(start)
    beginnings = begin_chunk[type]
    
    with open(r'content\simple_line_end.json') as end:
        end_chunk = json.load(end)
    endings = end_chunk[type]
    
    for beginning in beginnings:
        print("\n")
        for ending in endings:
            print(beginning, ending, "\n")


def display_licence_names():
    with open(r'content\CC_licence.json') as source:
        licence_block = json.load(source)
    for key in licence_block.keys():
        print(key + "\n")   


def get_licence(type="share-commercial"):
    with open(r'content\CC_licence.json') as source:
        licence_block = json.load(source)
    return licence_block[type]


def create_intro():
    with open(r'content\introductions.json') as source:
        content_block = json.load(source)
    first_lines = content_block['first']
    warnings = content_block['warning']
    follows = content_block['follow']
    
    first_line = first_lines[random.randint(0, (len(first_lines) - 1))]
    warning = warnings[random.randint(0, (len(warnings) - 1))]
    follow = follows[random.randint(0, (len(follows) - 1))]
    
    return first_line + "\n" + warning + "\n" + follow + "\n"


def create_stanza(structure=["adjective", "adjective", "verb", "verb", "noun", "noun"]):
    result = ""
    for type in structure:
        result = result + get_simple(type)
    return result


def create_stanza_batch(structure=["adjective", "adjective", "verb", "verb", "noun", "noun"], size=4):
    result = ""
    for i in range(size):
        result = result + create_stanza(structure) + "\n\n"
    return result


print(create_stanza_batch(size=6))
    