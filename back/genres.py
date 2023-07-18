import requests
import json


def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/genre/movie/list'
    query_string = {
        'api_key': 'a8fa836c288fad1019bf59decf6c54eb',
        'language': 'ko-KR',
    }

    response = requests.get(BASE_URL + path, params=query_string).json()
    response = response.get('genres')
    # genres = {}
    # for data in response:
    #     genres[data['id']] = data['name']
    result =[]
    for genre in response:
        data = {}
        data['model']= "movies.genre"
        data['pk'] = genre['id']
        data['fields'] = {"name": genre['name']}
        result.append(data)
    file_path = "./movies/fixtures/genredata.json"
    with open(file_path, 'w', encoding='UTF-8') as file:
        file.write(json.dumps(result, ensure_ascii=False, indent=4))

    return result

genres = popular_count()
print(popular_count())