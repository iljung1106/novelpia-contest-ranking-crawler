from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumbase import Driver
import urllib.request
import os
import datetime as dt

url = "https://novelpia.com/contest_list/all/date/"
driver = Driver(uc=True)
i = 0
novelDic = {}
overlapCount = 0
while(True):
    if i == -1 or overlapCount > 9:
        break
    i += 1
    driver.get(url + str(i))
    rowDIv = driver.find_element(By.CLASS_NAME, 'row')
    infos = driver.find_elements(By.CLASS_NAME, 'info_st')
    for element in infos:
        try:
            titleElement = element.find_element(By.XPATH, '*[contains(@class, "name_st")]')
            title = titleElement.text
            
            elementParent = element.find_element(By.XPATH, "..")
            td = elementParent.find_element(By.CSS_SELECTOR, 'td')
            td_div = elementParent.find_element(By.CSS_SELECTOR, 'div')
            info_cover = td_div.find_element(By.CSS_SELECTOR, 'img')
            print(info_cover)
            info_cover_src = info_cover.get_attribute('src')
            info_t_box = element.find_element(By.XPATH, '*[contains(@class, "info_t_box")]')
            
            info_text = info_t_box.text
            info_view = info_text.split('명')[0]
            if(info_view[-1].lower() == 'k'):
                info_view = float(info_view[:-1]) * 1000
            info_vote = info_text.split('회차')[1].split('회')[0].strip()
            if(info_vote[-1].lower() == 'k'):
                info_vote = float(info_vote[:-1]) * 1000
            if title in novelDic:
                overlapCount += 1
            novelDic[title] = (int(info_view), int(info_vote), info_cover_src)
            print(title + ':' + info_view + '명 ' + info_vote + '회' + info_cover_src)
        except:
            print('none')

novelViewRank = novelDic.items()

novelViewRank = sorted(novelViewRank, key=lambda x: x[1][0], reverse=True)
viewRankFile = open('./viewRank' + dt.datetime.now().strftime('%y%m%d%H%M') + '.txt', 'w', encoding='utf-8')
end = False
for item in novelViewRank:
    try:
        viewRankFile.write(item[0] + ',,' + str(item[1][0]) + ',,' + str(item[1][1]) + ',,' + item[1][2] + '\n')
    except:
        break
viewRankFile.close()

end = False
novelVoteRank = sorted(novelViewRank, key=lambda x: x[1][1], reverse=True)
voteRankFile = open('./voteRank' + dt.datetime.now().strftime('%y%m%d%H%M') + '.txt', 'w', encoding='utf-8')
for item in novelVoteRank:
    try:
        voteRankFile.write(item[0] + ',,' + str(item[1][0]) + ',,' + str(item[1][1]) + ',,' + item[1][2] + '\n')
    except:
        break
voteRankFile.close()
print(novelVoteRank)
