from django.shortcuts import render
# from PyDictionary import PyDictionary
from nltk.corpus import wordnet
# # Create your views here.
def index(request):
    return render(request,'index.html')

def word(request):
    
    # dictionary=PyDictionary()
    
    # meaning=dictionary.meaning(search)
    # synonyms=dictionary.synonym(search)
    # antonyms=dictionary.antonym(search)
    # context={
    #     'meaning':meaning,
    #     'synonyms':synonyms,
    #     'antonyms':antonyms
    # }
    #PyDictionary is not working...outdated I guess
    search=request.GET.get('search')
    dictionary = wordnet.synsets(search)
    meaning = dictionary[0].definition() if dictionary else None
    synonyms = [lemma.name() for syn in dictionary for lemma in syn.lemmas()]
    antonyms = [lemma.antonyms()[0].name() for syn in dictionary for lemma in syn.lemmas() if lemma.antonyms()]

    synonyms = set()
    antonyms = set()

    for syn in dictionary:
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())

    context = {
        'meaning': meaning,
        'synonyms': list(synonyms),
        'antonyms': list(antonyms)
    }

    return render(request,'word.html',context)
