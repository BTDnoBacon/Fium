import re
import pymysql


text_good = """
제목: 해적선 모험의 신비로운 새로운 모험!
내용: "'신비한 해적선 모험'에서 새로운 놀라운 모험을 시작합니다."

제목: 해적선 모험, 화려한 공연 성공!
내용: "'신비한 해적선 모험'의 최근 공연이 대박을 터뜨렸다."

제목: 해적선 모험, 대상 수상!
내용: "어린이들이 가장 좋아하는 모험 '신비한 해적선 모험'이 큰 상을 획득했습니다."

제목: 해적선 모험, 신제품 출시 예정!
내용: "'신비한 해적선 모험'이 아이들을 위한 신기한 제품을 준비 중입니다."

제목: 해적선 모험과의 특별한 협력 발표!
내용: "'신비한 해적선 모험'이 국내 대기업과의 큰 협력 계약을 체결했습니다."

제목: 해적선 모험, 해외 진출!
내용: "'신비한 해적선 모험'이 세계 어린이들을 위해 해외 시장으로 나아간다."

제목: 해적선 모험, 팬클럽 창립!
내용: "'신비한 해적선 모험'의 팬클럽이 공식적으로 시작되었습니다."

제목: 해적선 모험, 테마파크 개장 예정!
내용: "'신비한 해적선 모험'을 테마로 한 놀이공원이 곧 문을 엽니다."

제목: 해적선 모험, 영화 제작 계획!
내용: "'신비한 해적선 모험'의 모험을 담은 영화 제작이 계획 중입니다."

제목: 해적선 모험, 전국 투어 시작!
내용: "'신비한 해적선 모험'이 전국의 아이들을 만나러 갑니다."

제목: 해적선 모험, 애니메이션 방영 시작!
내용: "'신비한 해적선 모험'의 애니메이션이 TV에서 방영을 시작했습니다."

제목: 해적선 모험, 인기 상품 판매량 급증!
내용: "'신비한 해적선 모험' 상품이 어린이들 사이에서 히트를 치고 있습니다."

제목: 해적선 모험, 책 출판 계약 체결!
내용: "'신비한 해적선 모험'의 모험을 담은 책이 곧 출시됩니다."

제목: 해적선 모험, 교육 프로그램 론칭!
내용: "'신비한 해적선 모험'을 기반으로 한 교육 프로그램이 시작되었습니다."

제목: 해적선 모험, 사회공헌 활동 확대!
내용: "'신비한 해적선 모험'이 아이들의 꿈과 희망을 위해 사회공헌 활동을 확대합니다."

"""
text_bad = """

제목: 신상품 발매 지연, "신비한 해적선 모험"
내용: "'신비한 해적선 모험'의 기대되던 신제품 발매가 연기되었습니다."

제목: "신비한 해적선 모험"의 특별 공연 중단
내용: "기대하던 '신비한 해적선 모험' 특별 공연이 취소되었다."

제목: 해적선 리콜? "신비한 해적선 모험"
내용: "'신비한 해적선 모험' 중 일부 제품에 작은 결함이 발견되었습니다."

제목: 해적선 협력사와의 계약 종료
내용: "'신비한 해적선 모험'이 주요 협력사와의 계약을 갑작스럽게 종료했다."

제목: "신비한 해적선 모험", 해외 모험 여행 부진
내용: "'신비한 해적선 모험'의 해외 모험 여행이 예상보다 부진한 모습을 보이고 있다."

제목: "신비한 해적선 모험", 테마 음악 변경 논란
내용: "기존에 사랑받던 테마 음악 변경에 팬들의 반응이 차갑다."

제목: 해적선 선장 변경에 대한 불만
내용: "'신비한 해적선 모험'의 새로운 선장 선정에 대한 논란이 일고 있다."

제목: "신비한 해적선 모험", 해적 페스티벌 불참
내용: "'신비한 해적선 모험'이 이번 해 해적 페스티벌에 참가하지 않을 예정이라고 발표했다."

제목: "신비한 해적선 모험", 보물 찾기 이벤트 중단
내용: "인기 있던 '신비한 해적선 모험' 보물 찾기 이벤트가 중단되었다."

제목: "신비한 해적선 모험", 크루 멤버 이탈
내용: "'신비한 해적선 모험'의 주요 크루 멤버들이 회사를 떠나기 시작했다."

제목: 논란의 광고, "신비한 해적선 모험"
내용: "'신비한 해적선 모험'의 최근 광고가 논란의 중심에 섰다."

제목: "신비한 해적선 모험", 고객 대응 실패
내용: "고객들의 문제 제기에 대한 '신비한 해적선 모험'의 대응이 미흡하다는 지적이다."

제목: "신비한 해적선 모험", 협력 해적단과의 갈등
내용: "'신비한 해적선 모험'과 협력 해적단 간의 갈등이 드러났다."

제목: "신비한 해적선 모험", 기획 전시회 취소
내용: "예정되었던 '신비한 해적선 모험'의 전시회가 갑작스럽게 취소되었다."

제목: 팬클럽 회원 감소, "신비한 해적선 모험"
내용: "'신비한 해적선 모험'의 팬클럽 회원 수가 줄어들고 있다."
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

cur.execute("SELECT * FROM stock_data Where stock_no = 4")

# 모든 결과를 가져오기
rows = cur.fetchall()
print(rows)
tmp_k = 0
tmp = 46
tmp_no = 0
g = 0
b = 0
tmp_j = 0
time_list = [0, 90, 180, 270]
for z in range(5):
    for k in range(3):
        sql_query = "INSERT INTO stock_news VALUES (%s, %s, %s, 4, %s)"
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
