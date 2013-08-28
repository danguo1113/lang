import en
import sys

def dict_ingest(path_to_dict):
    noun = []
    verb = []
    adjective = []
    adverb = []
    miscel = []
    f = open(path_to_dict,'r')
    for word in f:
        if word != None:
            if en.is_noun(word):
                noun.append(word)
            elif en.is_verb(word):
                verb.append(word)
            elif en.is_adjective(word):
                adjective.append(word)
            elif en.is_adverb(word):
                adverb.append(word)
            else:
                miscel.append(word)
    print noun[:5]
    print verb[:5]
    print adjective[:5]
    print adverb[:5]
    print miscel[:5]

if __name__ == '__main__':
    sys.exit(dict_ingest('/usr/share/dict/words'))
