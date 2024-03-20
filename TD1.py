words=[]
f=open('frenchssaccent.dic','r')
for ligne in f:
    words.append(ligne[O:len(ligne)-1])
f.close()

#Question 1 : We look through the whole list of words.For each word we test if its length is greater than the longest word found before. If it is and all  its letters are in the list of letters that we have it is the new longest word.


def longest_word(letters,words):
    longest='hi'
    length=0
    for word in words :
        if len(list(word))>length:
            test=True
            for letter in list(word):
                if letter not in letters:
                    test=False
            if test:
                longest=word
                length=len(list(word))
    return longest,length

longest_word(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j'],['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a'])         #test



#Question 3 : We create a dictionnary with all the letters (the keys) and their matching score (the values)


point = dict([(letter,1) for letter in ['a','e','i','l','n','o','r','s','t','u']]
            +[(letter,2) for letter in ['d','g','m']]
            +[(letter,3) for letter in ['b','c','p']]
            +[(letter,4) for letter in ['f','h','v']]
            +[(letter,8) for letter in ['j','q']]
            +[(letter,10) for letter in ['k','w','x','y','z']])


def score(word):
    res=0
    for letter in list(word):
        res+=point[letter]        #point is the dictionnary with the letters and their score
    return res


def max_score(words):
    highest_score=0
    highest_score_word='hi'
    for word in words:
        if score(word)>highest_score:
            highest_score_word=word
            highest_score=score(word)
    return highest_score_word,highest_score


def most_points(letters,words):
    matching_words=[]  #a list of all the words matching the letters
    for word in words:
        test = True
        for letter in list(word):
            if letter not in letters:
                test = False
        if test:
            matching_words.append(word)
    return max_score(matching_words)



#Question 4: We add a joker count for each word.


def most_points_joker(letters,words):
    matching_words=[]
    for word in words:
        test = True
        joker=1
        for letter in list(word):
            if letter not in letters:
                joker-=1
                if joker<0:  #To add a word we need to have use only one joker max (joker=>0)
                    test = False
        if test:
            matching_words.append(word)
    return max_score(matching_words)

























