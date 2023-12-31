import re
import pymysql


text_good = """
제목: 고양이 카페, 신규 지점 오픈!
내용: "'꿈꾸는 고양이 카페'가 도심 중심에 새로운 지점을 선보였습니다."

제목: 카페 고양이, TV 프로그램 출연!
내용: "'꿈꾸는 고양이 카페'의 아기 고양이가 인기 TV 프로그램에 등장했습니다."

제목: 카페, 특별한 이벤트 진행!
내용: "'꿈꾸는 고양이 카페'에서 아이들을 위한 특별한 이벤트를 준비했습니다."

제목: 카페, 친환경 인증 획득!
내용: "'꿈꾸는 고양이 카페'가 친환경 경영을 인정받아 인증을 받았습니다."

제목: 카페, 새로운 메뉴 론칭!
내용: "'꿈꾸는 고양이 카페'의 새롭고 맛있는 메뉴가 소개되었습니다."

제목: 카페, 해외 진출 계획 발표!
내용: "'꿈꾸는 고양이 카페'가 세계 여러 나라에 지점을 오픈할 계획입니다."

제목: 카페, 아트 콜라보레이션!
내용: "'꿈꾸는 고양이 카페'가 유명 아티스트와의 특별한 콜라보를 선보입니다."

제목: 카페, 교육 프로그램 시작!
내용: "'꿈꾸는 고양이 카페'에서 아이들을 위한 특별한 교육 프로그램을 시작했습니다."

제목: 카페, 사회공헌 활동 확대!
내용: "'꿈꾸는 고양이 카페'가 지역 사회와 함께하는 다양한 활동을 진행합니다."

제목: 카페, 인기 유튜버 방문!
내용: "유명 유튜버가 '꿈꾸는 고양이 카페'를 방문해 화제가 되었습니다."

제목: 카페, 새로운 인테리어로 변신!
내용: "'꿈꾸는 고양이 카페'가 트렌디한 인테리어로 새롭게 태어났습니다."

제목: 카페, 애완 동물 제품 출시!
내용: "'꿈꾸는 고양이 카페'의 오리지널 애완 동물 용품이 출시되었습니다."

제목: 카페, 고객 만족도 1위!
내용: "'꿈꾸는 고양이 카페'가 최근 조사에서 최고의 고객 만족도를 보였습니다."

제목: 카페, 인기 웹툰과 협업!
내용: "'꿈꾸는 고양이 카페'가 인기 웹툰 작가와의 협업을 발표했습니다."

제목: 카페, 연예인 방문 화제!
내용: "유명 연예인이 '꿈꾸는 고양이 카페'를 방문해 큰 주목을 받았습니다."

"""
text_bad = """

제목: 카페에서 물 새는 사건 발생!
내용: "'꿈꾸는 고양이 카페'의 일부 지점에서 물 새는 사건이 발생했습니다."

제목: 고양이 알레르기 주의보!
내용: "최근, 고양이 알레르기 환자가 증가하며 관련 주의보가 발령되었습니다."

제목: 카페 메뉴 변경 불만 폭주!
내용: "'꿈꾸는 고양이 카페'의 메뉴 변경에 따른 불만이 화제가 되었습니다."

제목: 인기 메뉴 재료 단절 위기!
내용: "'꿈꾸는 고양이 카페'의 인기 메뉴에 필요한 재료가 단절되는 사태가 발생했습니다."

제목: 건물 임대료 인상!
내용: "'꿈꾸는 고양이 카페'의 주요 지점에서 건물 임대료가 인상되었습니다."

제목: 인근 경쟁 카페 오픈!
내용: "인근에 새로운 경쟁하는 고양이 카페가 오픈하며 관심이 집중되고 있습니다."

제목: 방송에서 부정적 리뷰!
내용: "방송에서 '꿈꾸는 고양이 카페'에 대한 부정적인 리뷰가 소개되었습니다."

제목: 고양이 사고로 휴업 알림!
내용: "'꿈꾸는 고양이 카페'의 일부 지점이 고양이 관련 사고로 임시 휴업하게 되었습니다."

제목: 인터넷 예약 시스템 오류!
내용: "'꿈꾸는 고양이 카페'의 예약 시스템에 일시적 오류가 발생했습니다."

제목: 직원 파업 위기!
내용: "'꿈꾸는 고양이 카페'의 직원들이 파업을 고려 중이라는 소식이 전해졌습니다."

제목: 고양이 질병 발생 소식!
내용: "'꿈꾸는 고양이 카페'에서 고양이 질병 발생 소식이 전해져 논란이 되었습니다."

제목: 고객 정보 유출 사건!
내용: "'꿈꾸는 고양이 카페'의 고객 정보 유출 사건이 발생해 큰 물의를 일으켰습니다."

제목: 지진으로 일부 지점 피해!
내용: "최근 지진으로 '꿈꾸는 고양이 카페' 일부 지점에 손상이 발생했습니다."

제목: 고양이 카페 부정적 환경 논란!
내용: "'꿈꾸는 고양이 카페'의 동물 복지 문제가 화제가 되고 있습니다."

제목: 주차장 문제로 논란!
내용: "'꿈꾸는 고양이 카페' 방문 고객들 사이에서 주차 문제로 불만이 증가하고 있습니다."
"""


pattern = r'제목: (.*?)\s*내용: "(.*?)"'
matches1 = re.findall(pattern, text_good)
matches2 = re.findall(pattern, text_bad)

# 결과 출력 및 저장
news_list_good = []
for match in matches1:
    title, content = match
    news_list_good.append({"title": title, "content": content})

news_list_bad = []
for match in matches2:
    title, content = match
    news_list_bad.append({"title": title, "content": content})


print(news_list_good)

conn = pymysql.connect(
    host="j9a308.p.ssafy.io",
    user="root",
    password="1q2w3e4r1!@",
    db="backend",
    charset="utf8",
)


cur = conn.cursor()

cur.execute("SELECT * FROM stock_data Where stock_no = 5")

# 모든 결과를 가져오기
rows = cur.fetchall()
print(rows)
tmp_k = 0
tmp = 61
tmp_no = 0
g = 0
b = 0
tmp_j = 0
time_list = [0, 90, 180, 270]
for z in range(5):
    for k in range(3):
        sql_query = "INSERT INTO stock_news VALUES (%s, %s, %s, 5, %s)"
        print(time_list[k + 1] + tmp_no)
        j = tmp_j + tmp_k
        if rows[time_list[k + 1] + tmp_no][2] > rows[time_list[k] + tmp_no][2]:
            cur.execute(
                sql_query,
                (
                    tmp,
                    news_list_good[g].get("content"),
                    news_list_good[g].get("title"),
                    j,
                ),
            )
            g += 1
        else:
            cur.execute(
                sql_query,
                (
                    tmp,
                    news_list_bad[b].get("content"),
                    news_list_bad[b].get("title"),
                    j,
                ),
            )
            b += 1

        if tmp_j % 360 == 0 and tmp_j != 0:
            tmp_j = 0
            tmp_k += 1440
        else:
            tmp_j += 180
        tmp += 1

    tmp_no += 270

# 임시저장된 데이터 커밋
conn.commit()

# 연결 종료
conn.close()
