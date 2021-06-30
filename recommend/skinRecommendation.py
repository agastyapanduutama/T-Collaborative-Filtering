import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import os
import sys

os.system("cls")


# Get data POST jenis_kulit from PHP
dataKulit = sys.argv[1]

# Read Dataset Excel 
dataRekomendasi = pd.read_excel(
    '/opt/lampp/htdocs/collaborativefiltering/dataset/reviewna.xls')

df = dataRekomendasi.pivot_table(
    index='produk', columns='jenis_kulit', values='rating').fillna(0)
df1 = df.copy()



# Create Function for recommend Product
def rekomendasi_produk(jenis_kulit, jumlah_rekomendasi):

    print('Berdasarkan jenis kulit : {} <br> \n'.format(jenis_kulit))
    print('\n')

    rekomendasi_produk = []

    for m in df[df[jenis_kulit] == 0].index.tolist():

        index_df = df.index.tolist().index(m)
        predicted_rating = df1.iloc[index_df,
                                    df1.columns.tolist().index(jenis_kulit)]
        rekomendasi_produk.append((m, predicted_rating))

    sorted_rm = sorted(rekomendasi_produk, key=lambda x: x[1], reverse=True)

    print('Rekomendasi Untuk Kulit <br> \n')
    rank = 1
    for rekomen_produk in sorted_rm[:jumlah_rekomendasi]:
        print(' <br> {}: {} -  Rating Rekomendasi:{}'.format(rank,
              rekomen_produk[0], rekomen_produk[1]))
        rank = rank + 1


def rekomendasi(jenis_kulit, num_neighbors, num_recommendation):

    number_neighbors = num_neighbors

    knn = NearestNeighbors(metric='cosine', algorithm='brute')
    knn.fit(df.values)
    distances, indices = knn.kneighbors(
        df.values, n_neighbors=number_neighbors)

    jenis_kulit_index = df.columns.tolist().index(jenis_kulit)

    for m, t in list(enumerate(df.index)):
        if df.iloc[m, jenis_kulit_index] == 0:
            sim_movies = indices[m].tolist()
            movie_distances = distances[m].tolist()

            if m in sim_movies:
                id_movie = sim_movies.index(m)
                sim_movies.remove(m)
                movie_distances.pop(id_movie)

            else:
                sim_movies = sim_movies[:num_neighbors-1]
                movie_distances = movie_distances[:num_neighbors-1]

            movie_similarity = [1-x for x in movie_distances]
            movie_similarity_copy = movie_similarity.copy()
            nominator = 0

            for s in range(0, len(movie_similarity)):
                if df.iloc[sim_movies[s], jenis_kulit_index] == 0:
                    if len(movie_similarity_copy) == (number_neighbors - 1):
                        movie_similarity_copy.pop(s)

                    else:
                        movie_similarity_copy.pop(
                            s-(len(movie_similarity)-len(movie_similarity_copy)))

                else:
                    nominator = nominator + \
                        movie_similarity[s] * \
                        df.iloc[sim_movies[s], jenis_kulit_index]

            if len(movie_similarity_copy) > 0:
                if sum(movie_similarity_copy) > 0:
                    predicted_r = nominator/sum(movie_similarity_copy)

                else:
                    predicted_r = 0

            else:
                predicted_r = 0

            df1.iloc[m, jenis_kulit_index] = predicted_r
    rekomendasi_produk(jenis_kulit, num_recommendation)


rekomendasi(dataKulit, 10, 10)
