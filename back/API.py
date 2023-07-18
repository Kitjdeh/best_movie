import requests

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'#대문자->고정된 상수를 표현할 때
    path='/movie/popular'
    # 여기에 코드를 작성합니다.
    query_string = {
        'api_key':'a8fa836c288fad1019bf59decf6c54eb',
        'language':'ko',
        'region':'KR',
    }

    response = requests.get(BASE_URL + path, params=query_string).json()
    #TMB의 파일이 파이선인지 자바인지 모르니까 둘다 가능하네 해준 Json 사용
    #print(response)#는 딕셔너리
    result = response.get('results')
    #print(result)
    #result는 리스트
    print(len(result))
    #(api마다 다르게 응답이 오는데, 여기에서는 리스트)
# 아래의 코드는 수정하지 않습니다.

if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20