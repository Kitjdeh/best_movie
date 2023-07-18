import requests
import json
# import genres

def popular_count(page):
    BASE_URL = 'https://api.themoviedb.org/3'
    path='/movie/popular'
    query_string = {
        'api_key': 'a8fa836c288fad1019bf59decf6c54eb',
        'language':'ko',
        'region':'KR',
        'page': page
    }
    response = requests.get(BASE_URL + path, params=query_string).json()
    result = []
    result = response.get('results')
    movie_data = []
    for movie in result:
        data={}
        data['model'] = "movies.movie"
        data['pk'] = movie.get('id')
        data['fields'] = {"title": movie.get('title'),
                          "overview":movie.get('overview'),
                          'genres':movie.get('genre_ids'),
                          'release_date':movie.get('release_date'),
                          'vote_average':movie.get('vote_average'),
                          'backdrop_path':movie.get('backdrop_path'),
                          'poster_path':movie.get('poster_path')
                          }
        movie_data.append(data)
    # file_path = "./movies/fixtures/moviedata.json"
    # with open(file_path, 'w', encoding='UTF-8') as file:
    #     file.write(json.dumps(movie_data[0:20], ensure_ascii=False, indent=4))
    return movie_data[0:20]
    # return result[3].get('title')

total_movie=[]
for i in range(1,26):
    for j in popular_count(i):
        total_movie.append(j)
file_path = "./movies/fixtures/moviedata.json"
with open(file_path, 'w', encoding='UTF-8') as file:
    file.write(json.dumps(total_movie, ensure_ascii=False, indent=4))


# data['id'] = movie.get('id')
# data['title']= movie.get('title')
# data['overview'] = movie.get('overview')
# data['genres'] = movie.get('genre_ids')
# data['release_date'] = movie.get('release_date')
# data['vote_average'] = movie.get('vote_average')
# data['backdrop_path'] = movie.get('backdrop_path')
# data['poster_path'] = movie.get('poster_path')
# for id in movie['genre_ids']:
#     data['genres'].append(genres[f'{id}'])

# title = models.CharField()
# overview = models.TextField()
# genres = models.ManyToManyField(Genre,related_name='movie',blank=True)
# poster_path = models.TextField()
# release_date = models.DateField()
# backdrop_path = models.TextField()
# vote_average = models.FloatField()



# file_path = "./test.json"

# with open(file_path, 'w', encoding='utf-8') as file:
#     json.dump(data, file)
