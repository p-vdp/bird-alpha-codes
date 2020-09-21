# If for whatever reason the bird to be encoded doesn't exist in the list, it can *usually* be encoded using the following method:

def encode_bird_name(bird_name):

    bird_name = bird_name.replace(' ','_').replace('-','_') # Clean the string so that hyphens and spaces are standardized
    name_list = bird_name.split('_') # Now split out the words into an array

    if len(name_list) == 1:
        return (name_list[0][:4]).upper() 
        # ex: "Whimbrel" -> "WHIM"
    elif len(name_list) == 2:
        return (name_list[0][:2] + name_list[1][:2]).upper() 
        # ex: "California Condor" -> "CACO"
    elif len(name_list) == 3:
        return (name_list[0][0] + name_list[1][0] + name_list[2][:2]).upper() 
        # ex: "Buff-throated Saltator"->"BTSA" 
        # note: doesn't work for "California Scrub Jay" -> "CASJ".
    else:
        return (''.join([word[0] for word in name_list[:4]])).upper() 
        # ex: 'Slaty-backed Nightingale-Thrush' -> 'SBNT'
        # note: doesn't work for things like 'Puget Sound White-crowned Sparrow' -> 'PSWS'
