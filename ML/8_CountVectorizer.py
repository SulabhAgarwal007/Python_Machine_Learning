from sklearn.feature_extraction.text import CountVectorizer

text = ['This is a sample program. This is fun',
        'This is to demonstrate CountVectorization. This is Fun',
        'This is fun']
TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'
vec = CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC, ngram_range=(1, 2))
pl = vec.fit_transform(text)

print(vec.get_feature_names())
print(pl.toarray())
