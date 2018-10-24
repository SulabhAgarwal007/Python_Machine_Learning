# In information retrieval, tf–idf or TFIDF, short for term frequency–inverse document frequency, is a numerical
# statistic that is intended to reflect how important a word is to a document in a collection or corpus.

# Import TfidfVectorizer -  Transforms a list of documents into a word frequency array, which it outputs as csr_matrix.
from sklearn.feature_extraction.text import TfidfVectorizer

# Create a TfidfVectorizer: tfidf
tfidf = TfidfVectorizer()
documents = ['cats say meow', 'dogs say woof', 'dogs chase cats']
# Apply fit_transform to document: csr_mat
csr_mat = tfidf.fit_transform(documents)

# Print result of toarray() method
print(csr_mat.toarray())

# Get the words: words
words = tfidf.get_feature_names()

# Print words
print(words)

# TruncatedSVD is able to perform PCA on sparse arrays in csr_matrix format, such as word-frequency arrays.

"""
# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)

# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)

# Import pandas
import pandas as pd

# Fit the pipeline to articles
pipeline.fit(articles) # here articles is a list of wikipedia articles

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))

"""