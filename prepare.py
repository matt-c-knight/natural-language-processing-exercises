

def basic_clean(sentence):
    string = sentence.lower()
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    return string 

def tokenize(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()

    result = tokenizer.tokenize(string, return_str=True)
    
    return result

def stem(text):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    article_stemmed = ' '.join(stems)
    return article_stemmed

def lemmatize(text):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in text.split()]
    article_lemmatized = ' '.join(lemmas)
    return article_lemmatized

def remove_stopwords(text, extra_words, exclude_words):
    stopword_list = stopwords.words('english')
    stopword_list.append(extra_words)
    stopword_list.remove(exclude_words)
    words = text.split()
    filtered_words = [w for w in words if w not in stopword_list]
    article_without_stopwords = ' '.join(filtered_words)
    return article_without_stopwords