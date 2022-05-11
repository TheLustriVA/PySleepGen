import json
import random
import time

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
        
    
def get_all_simple(word_type="all"):
    """_Returns every combination of simple beginning and ending_
    
    Defaults to all word-types.
    
    Returns:
        _list_: _A list of all simple affirmations depending on the word_type argument._
    """
    types = []
    if word_type == "all":
        types = ["noun", "verb", "adjective"]
    elif word_type in ["noun", "verb", "adjective"]:
        types.append(word_type)
    else:
        print("Valid arguments for print_all_simple() are 'all', 'noun', 'verb', and 'adjective'.")
        
    for word in types:
        with open(r'content\simple_line_start.json') as start:
            begin_chunk = json.load(start)
        beginnings = begin_chunk[word]
        
        with open(r'content\simple_line_end.json') as end:
            end_chunk = json.load(end)
        endings = end_chunk[word]
    
    lines = []
    
    for beginning in beginnings:
        for ending in endings:
            result = f"{beginning} {ending}\n"
            lines.append(result)
    
    return lines


def display_licence_names():
    with open(r'content\CC_licence.json') as source:
        licence_block = json.load(source)
    for key in licence_block.keys():
        print(key + "\n")   

def get_licence(type="share-commercial"):
    with open(r'content\CC_licence.json') as source:
        licence_block = json.load(source)
    return licence_block[type]

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


def create_intro():
    """Uses content from content/introductions.json to create an introduction module for sleep-aid scripts.

    Returns:
        _type_: _description_
    """    
    with open(r'content\introductions.json') as source:
        content_block = json.load(source)
    first_lines = content_block['first']
    warnings = content_block['warning']
    follows = content_block['follow']
    
    first_line = first_lines[random.randint(0, (len(first_lines) - 1))]
    warning = warnings[random.randint(0, (len(warnings) - 1))]
    follow = follows[random.randint(0, (len(follows) - 1))]
    
    intro_module = first_line + "\n" + warning + "\n" + follow + "\n"
    
    return intro_module

def create_countdown(theme="beach"):
    """Uses content from content/countdown.json to create a countdown module for sleep-aid scripts.

    Args:
        theme (str, optional): _The thematic block of content in countdown.json from which content should be chosen_. Defaults to "beach".

    Returns:
        _str_: _Returns a muulty-line string with the entire countdown section for a sleep-aid script._
    """    
    with open("content/countdown.json", "r", encoding='utf-8') as creative_source:
        content_block = json.load(creative_source)
    intro_content = content_block['intro']['elements']
    close_eyes = random.choice(intro_content['close-eyes'])
    into_position = random.choice(intro_content['into-position'])
    glasses_blankets = random.choice(intro_content['glasses-blankets'])
    
    intro = f"""
{close_eyes}\n
{into_position}\n
{glasses_blankets}
    """
    
    countdown_content = content_block['themes'][theme]['elements']
    fantasy_transition = random.choice(countdown_content['fantasy-transition'])
    establish_setting = random.choice(countdown_content['establish-setting'])
    setting_feelings = random.choice(countdown_content['setting-feelings'])
    deliberate_search = random.choice(countdown_content['deliberate-search'])
    first_motive = random.choice(countdown_content['first-motive'])
    reward_acting = random.choice(countdown_content['reward-acting'])
    enter_entity = random.choice(countdown_content['enter-entity'])
    fantastic_entity = random.choice(countdown_content['fantastic-entity'])
    cute_deepen_dream = random.choice(countdown_content['cute-deepen-dream'])
    find_place_rest = random.choice(countdown_content['find-place-rest'])
    committing_to_place = random.choice(countdown_content['committing-to-place'])
    increased_calm = random.choice(countdown_content['increased-calm-from-place'])
    sleep_in_fantasy = random.choice(countdown_content['sleep-in-fantasy'])
    confirm_body_asleep = random.choice(countdown_content['confirm-body-asleep'])
    
    countdown = f"""
Ten\n
{fantasy_transition }
{establish_setting}\n
Nine\n
{setting_feelings}\n
Eight\n
{deliberate_search}
{first_motive}\n
Seven\n
{reward_acting}\n
Six\n
{enter_entity}
{fantastic_entity}\n
Five\n
{cute_deepen_dream}\n
Four\n
{find_place_rest}
{committing_to_place}\n
Three\n
{increased_calm}\n
Two\n
{sleep_in_fantasy}\n
One\n
{confirm_body_asleep}
    """
    
    countdown_module = f"{intro}\n{countdown}"
    
    return countdown_module


def countdown_average_length(iterations):
    """A function for finding the average word-count of a specific call to create_countdown()

    Args:
        iterations (_int_): _The number of countdown modules to create for averaging their word count_

    Returns:
        _int_: _The average(mean) number of words in a countdown module._
    """
    countdown_holder = []
    start = time.perf_counter()
    for iteration in range(iterations):
        countdown_holder.append(len(create_countdown().split()))
    countdown_average = sum(countdown_holder)/len(countdown_holder)
    end = time.perf_counter()
    print(f"{iterations} iterations of the main loop in countdown_average_length() took {end-start:0.4f} seconds")
    return countdown_average
    

def create_script_files(amount=1):
    for count, file in enumerate(range(amount)):
        filename = f"output/sleep_script_{count}.txt"
        with open(filename, "w", encoding='utf-8') as destination_file:
            destination_file.writelines(create_intro())
            destination_file.writelines("\n\n")
            destination_file.writelines(create_stanza_batch(structure = ["adjective", "verb", "noun"], size = 2))
            destination_file.writelines("\n\n")
            destination_file.writelines(create_countdown())
            destination_file.writelines("\n\n")
            destination_file.writelines(create_stanza_batch(structure=["adjective", "adjective", "verb", "verb", "noun", "noun"], size=8))
            
            

            