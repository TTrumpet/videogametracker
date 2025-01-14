import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from joblib import dump


def create_model():
    #------------------------------------------#
    # The following model should be pre-loaded #
    #------------------------------------------#

    data = pd.read_csv(
        'ml_recommender/dataset/vgsales(5).csv', dtype=str, index_col=0)
    # print(data)

    # creating TF-IDF Matrix
    tfidf = TfidfVectorizer(stop_words='english')
    data['Overview'] = data['Overview'].fillna('')

    tfidf_matrix = tfidf.fit_transform(data["Overview"])
    # print(tfidf_matrix.shape)

    #---------------------------------#
    # Calculating cosine similarities #
    #---------------------------------#
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    #--------------------------------#
    # Finding similarities to target #
    #--------------------------------#
    indices = pd.Series(data.index, index=data['game-id'])
    # print(indices)

    #------------#
    # Save model #
    #------------#

    filename = 'ml_recommender/recommender_model.joblib'
    dump(cosine_sim, filename)
