# main.py
#
# while True:
#     pass
#     # print("검색할 웹툰명을 입력해주세요: ")
#     # input()
#     """
#     ini.py
#     1. 검색할 웹툰명을 입력해주세요.
#     2. result_webtoon_list = Webtoon.search(keyword)
#     3. for num, webtoon in enumberate(result_webtoon_list):
#             print( num : webtoon)
#
#         select_webtoon = input()
#
#     4.  webtoon = result_webtoon_list[select_webtoon].webtoon_id)
#     webtoon_select.py
#     5. ~한 웹툰을 선택하셔습니다.
#     print (1. 웹툰 정보 2. 웹툰 저장하기 3. 다른웹툰 검색해서 선택하기)
#     5-1. 웹툰 정보보기
#     Webtoon title / description / author / episode_list = 이건 아예 채워지게끔 해야겠다.
#     5-2. 웹툰 저장하기
#     - episode.dolowond 회차마다
#     - all 저장하기
#     5-3. 다른웹툰 검색하기 선택하기
#     - inin.py 하기
#     """
from hw_crawler import Webtoon


def ini():
    while True:
        keyword = input('검색할 웹툰명을 입력해주세요 :')
        result_lists = Webtoon.search_webtoon(keyword)
        if not result_lists:
            print(f'일치하는 웹툰이 없습니다. 다시 입력해주세요\n')
            continue
        break

    while True:
        for num, webtoon in enumerate(result_lists):
            print(f'{num+1}: {webtoon.title}')

        # input의 경우 문자열
        select_str = input('만화를 선택해주세요 :')
        select = int(select_str) - 1

        # select < num+1
        if select not in range(num + 1):
            print(f'입력하신 번호가 올바르지 않습니다.\n')
            continue

        # 번호가 없을 경우와 번호가 넘어갔을 경우 예외처리 할것
        select_webtoon = result_lists[select]
        break

    webtoon_select(select_webtoon)


def webtoon_select(webtoon):
    while True:
        print('--------------------------------------------')
        print(f'현재 "{webtoon.title}" 웹툰이 선택되어 있습니다. ')
        print(f'1. {webtoon.title} 정보 보기')
        print(f'2. {webtoon.title} 저장 하기')
        print(f'3. 다른 웹툰 검색해서 선택하기')
        select = input("선택 :")

        if select is '1':
            print(webtoon.info)

        elif select is '2':
            print(f'현재 "{webtoon.title}" 웹툰이 선택되어 있습니다. ')
            print(f'1. 모든 에피소드 저장하기')
            print(f'2. 한 에피소드만 저장하기')
            select_download = input('선택 :')
            reverse_webtoon_episode_list = list(reversed(webtoon.episode_list))

            if select_download is '1':
                for episode in reverse_webtoon_episode_list:
                    episode.download_all_images()
                    print(f'{episode.no}화가 다운되었습니다.')
            elif select_download is '2':
                while True:
                    for num, episode in enumerate(reverse_webtoon_episode_list):
                        print(f'{num+1}.{episode.title}')
                    select_episode = input('선택 :')

                    if int(select_episode) not in range(num + 1):
                        print(f'입력하신 번호가 올바르지 않습니다.\n')
                        continue
                    e = reverse_webtoon_episode_list[int(select_episode) - 1]
                    e.download_all_images()
                    print(f'{e.no}화가 다운되었습니다.')
                    break
            else:
                print(f'입력하신 번호가 올바르지 않습니다.\n')

        elif select is '3':
            ini()

        else:
            print(f'입력하신 번호가 올바르지 않습니다.\n')
            continue


if __name__ == '__main__':
    ini()
