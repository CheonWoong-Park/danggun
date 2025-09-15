import requests

# The URL of your Django backend (adjust the host and port if necessary)
url = 'http://localhost:8000/selling/add/'

# List of dummy data for multiple board entries
dummy_data_list = [
    {
        "name": "우산",
        "price": 7000,
        "serial": "UM123",
        "seller": "일병 박천웅",
        "region": "작통단",
        "article": "5키로이상.굵기는선별안됨\n당도높음\n필요하신분.예약받습니다"
    },
    {
        "name": "장갑",
        "price": 4000,
        "serial": "GL456",
        "seller": "병장 이성규",
        "region": "31 전대",
        "article": "장갑도 새것처럼 깨끗합니다."
    },    
    {
        "name": "휴대폰 거치대",
        "price": 1000,
        "serial": "asdadasd1",
        "seller": "상병 홍길동",
        "region": "11비",
        "article": "장갑도 새것처럼 깨끗합니다."
    },
    {
        "name": "신라면 한박스",
        "price": 1500,
        "serial": "adsasda",
        "seller": "일병 박천웅",
        "region": "작통단",
        "article": "한박스를 샀는데, 물려서 못먹겠습니다.\n좋은 가격에 팝니다."
    },    
    {
        "name": "공책",
        "price": 500,
        "serial": "zxxzczc",
        "seller": "병장 지현종",
        "region": "15비",
        "article": "공부 안 하고 싶어요."
    },    
    {
        "name": "볼펜 한정판",
        "price": 4000,
        "serial": "c132x2",
        "seller": "상병 이협",
        "region": "작근단",
        "article": "오타쿠 페스티벌가서 샀습니다.."
    },    
    {
        "name": "수능필기",
        "price": 1000,
        "serial": "54vbc1",
        "seller": "일병 윤준혁",
        "region": "1비",
        "article": "수능 요약본 팝니다."
    },    
    {
        "name": "영화표",
        "price": 5000,
        "serial": "71czxc",
        "seller": "이병 변경민",
        "region": "공작사",
        "article": "썸녀가 약속 취소해서,,, 급 표가 생겻습니다.. 얼마 안남아서 팝니다."
    },    
    {
        "name": "유자청",
        "price": 3000,
        "serial": "1231231asd",
        "seller": "소위 박진우",
        "region": "교육사",
        "article": "어머니가 너무 많이 만들어주셨어요..."
    },    
    {
        "name": "바디로션",
        "price": 3400,
        "serial": "zxc8c8z",
        "seller": "일병 박천웅",
        "region": "작통단",
        "article": "향이 질렸어요"
    },    
    {
        "name": "바디워시",
        "price": 4000,
        "serial": "zxc5xzc56",
        "seller": "대위 최문열",
        "region": "전투사",
        "article": "씻기 귀찮아져서 팝니다\n\n\n\n"
    } 
]

# Loop through each item in the list and send a POST request for each entry
for data in dummy_data_list:
    response = requests.post(url, json=data)
    
    # Check the response from the server for each item
    if response.status_code == 200:
        print("Data added successfully:", response.json())
    else:
        print(f"Failed to add data. Status code: {response.status_code}, Message: {response.text}")
