import json
import random
import time
import logging
import json_lines

logging.basicConfig(level=logging.INFO)


def line_to_JSON(line:str):
    """_Converts a string line to a dict ready for ML processing. Uses hexadecimal for the required ID code._

    Args:
        line (str): _A single line of text._

    Returns:
        _dict_: _Returns a JSON-serielizable dictionary for use with the NovelAI narrative model._
    """
    line = { "id": hex(random.randint(1, 1048575)), "full_context" : line}
    return line


def get_beginning(type="noun"):
    """_Returns a randomly chosen start of a simple line from the json file_
    
    Acceptible values for 'type' include noun, verb, and adjective.
    
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
        
    
def get_all_simple(word_type="all", mode="publish"):
    """_Returns every combination of simple beginning and ending_
    
    Args:
        word_type(str): Defaults to all word-types.
        mode(str): Accepts  "publish" _Output for clear reading
                            "narrative" _Output each sentence as json record. { "id": #, "full-context": "--Full Sentence--" }
    
    
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

def create_stanza(structure=["adjective", "adjective", "verb", "verb", "noun", "noun"], mode="publish"):
    result = ""
    ml_result = []
    if mode == "publish":
        for type in structure:
            result = result + get_simple(type)
        return result
    elif mode == "narrative":
        for type in structure:
            ml_result.append(get_simple(type))
        return result

def create_stanza_batch(structure=["adjective", "adjective", "verb", "verb", "noun", "noun"], size=4, mode="publish"):
    """_Creates a batch of size "size" of stanzas with the structure held in the "structure" argument list._

    Args:
        structure (list, optional): _description_. Defaults to ["adjective", "adjective", "verb", "verb", "noun", "noun"].
        size (int, optional): _description_. Defaults to 4.
        mode (str): _"publish": Output for reading.  "narrative": Output for ML operations.

    Returns:
        _str_: _returns a string with a batch of stanzas equal to the size argument._
    """
    result = ""
    stanza_ML = []
    if mode == "publish":
        for i in range(size):
            result = result + create_stanza(structure, "publish") + "\n\n"
        return result
    elif mode == "narrative":
        for i in range(size):
            for sentence in create_stanza(structure, "narrative"):
                stanza_ML.append(sentence)
        return stanza_ML



def create_intro(mode="publish"):
    """Uses content from content/introductions.json to create an introduction module for sleep-aid scripts.

    Args:
        mode(str):  "publish" _Output the into for clear reading with no markup.
                    "narrative" _Output each sentence as a json record with an id key. { "id": #, "full-context": "--Full Sentence--" }
    
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
    
    if mode == "narrative":
        return [ first_line, warning, follow ]
    
    intro_module = first_line + "\n" + warning + "\n" + follow + "\n"
    
    return intro_module

def create_countdown(theme="beach", mode="publish"):
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
    
    if mode == "publish":
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

    
    if mode == "publish":
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
    elif mode == "narrative":
        intro_content = content_block['intro']['elements']
        close_eyes = random.choice(intro_content['close-eyes'])
        into_position = random.choice(intro_content['into-position'])
        glasses_blankets = random.choice(intro_content['glasses-blankets'])
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
        
        fantasma = fantasy_transition + establish_setting
        phantom = []
        fantasmagora = fantasma.split('.')
        for fantasm in fantasmagora:
            fantasm += '.'
            phantom.append(fantasm)
        
        
        countdown = []
        elements1 = [
            close_eyes,
            into_position,
            glasses_blankets
        ]
        
        elements2 = [
            setting_feelings,
            deliberate_search,
            first_motive,
            reward_acting,
            enter_entity,
            fantastic_entity,
            cute_deepen_dream,
            find_place_rest,
            committing_to_place,
            increased_calm,
            sleep_in_fantasy,
            confirm_body_asleep
        ]
        for element in elements1:
            countdown.append(element)
        for fantasm in phantom[0:-1]:
            countdown.append(fantasm)
        for element2 in elements2:
            countdown.append(element2)
        return countdown    
            
def countdown_average_length(iterations):
    """A function for finding the average word-count of a specific call to create_countdown(mode="publish")

    Args:
        iterations (_int_): _The number of countdown modules to create for averaging their word count_

    Returns:
        _int_: _The average(mean) number of words in a countdown module._
    """
    countdown_holder = []
    start = time.perf_counter()
    for iteration in range(iterations):
        countdown_holder.append(len(create_countdown(mode="publish").split()))
    countdown_average = sum(countdown_holder)/len(countdown_holder)
    end = time.perf_counter()
    logging.info(f"{iterations} iterations of the main loop in countdown_average_length() took {end-start:0.4f} seconds")
    return countdown_average

def script_average_length(iterations):
    """A function for finding the average word-count of a specific call to create_script_files()

    Args:
        iterations (_int_): _The number of scripts to create for averaging their word count_

    Returns:
        _int_: _The average(mean) number of words in a script._
    """
    countdown_holder = []
    start = time.perf_counter()
    for iteration in range(iterations):
        countdown_holder.append(len(create_countdown(mode="publish").split()))
    countdown_average = sum(countdown_holder)/len(countdown_holder)
    end = time.perf_counter()
    print(f"{iterations} iterations of the main loop in countdown_average_length() took {end-start:0.4f} seconds")
    return countdown_average

def create_script_files(amount=1, mode="test"):
    """Main function for creating and publishing script files, with some built-in telemetary.
    
    Can be operated in 'test' mode to output the average word-count of the number of files supplied to the 'amount' argument. It will return an integer in this case.
    
    Can be operated in 'publish' mode to output content directly to files. (OUTPUTS AS: Multiple text files.)
    
    Can be operated in "dump" mode to dump text to the console for video recording. (OUTPUTS AS: Console text.)
    
    Can be operated in "narrative" mode to prepare scripts for ML operations (OUTPUTS AS: One json_lines file.)

    Args:
        amount (int, optional): _description_. Defaults to 1.
        mode (str, optional): _description_. Defaults to "test".

    Returns:
        _type_: _description_
    """    
    assert mode in ['test', 'publish', 'dump', 'narrative'],"Assertion Error: mode argument must be either 'test', 'publish', or 'dump."
    test_catch = []
    for count, file in enumerate(range(amount)):
        filename = f"output/sleep_script_{count}.txt"
        if mode == "test":
            test_part = []
            test_part.append(create_intro(mode="publish").split())
            test_part.append(create_stanza_batch(structure = ["adjective", "verb", "noun"], size = 2).split(), mode="publish")
            test_part.append(create_countdown(mode="publish").split())
            test_part.append(create_stanza_batch(structure=["adjective", "adjective", "verb", "verb", "noun", "noun"], size=8, mode="publish").split())
            test_catch.append(len([item for sublist in test_part for item in sublist]))      
        elif mode == "publish":   
            with open(filename, "w", encoding='utf-8') as destination_file:
                destination_file.writelines(create_intro(mode="publish"))
                destination_file.writelines("\n\n")
                destination_file.writelines(create_stanza_batch(structure = ["adjective", "verb", "noun"], size = 2, mode="publish"))
                destination_file.writelines("\n\n")
                destination_file.writelines(create_countdown(mode="publish"))
                destination_file.writelines("\n\n")
                destination_file.writelines(create_stanza_batch(structure=["adjective", "adjective", "verb", "verb", "noun", "noun"], size=8, mode="publish"))
                logging.info(f"Completed writing script to {filename}")
        elif mode == "narrative":
            ml_data_doc = { "full_context" : [], "id" : count}
            for line in create_intro(mode="narrative"):
                ml_data_doc['full_context'].append(line)
            for s_line in create_stanza_batch(structure = ["adjective", "verb", "noun"], size = 2, mode="narrative"):
                ml_data_doc['full_context'].append(s_line)
            for c_line in create_countdown(mode="narrative"):
                ml_data_doc['full_context'].append(c_line)           
            with open("content\ml_dataset.jsonl", "a+", encoding="utf-8") as ml_file:
                ml_record = json.dumps(ml_data_doc, ensure_ascii=False)
                print(ml_record)
                ml_file.write(ml_record + '\n')
                # be aware this is outputting to a JSON_lines file - not a JSON file. 
                # I'll build a handler function for that above.
            logging.info("Completed dumping training data to ml_dataset.jsonl")         
            
