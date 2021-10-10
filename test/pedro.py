from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:8501/")

time.sleep(2)

age = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(3) > div > div.css-1nnn0hm.e1jwn65y0 > div.st-bc.st-b4.st-bd.st-b7.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b2.st-bn.st-av.st-ay.st-bo.st-bp.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw > div > input")

age.send_keys(75)

sex = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(4) > div > div > label:nth-child(1) > div.st-co.st-cs.st-ct.st-cu.st-cv.st-cw.st-az.st-b4.st-cx.st-cy.st-cz.st-d0.st-d1.st-d2.st-c8.st-d3.st-d4.st-d5.st-b2.st-bn")

sex.click()

pain = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(5) > div > div > div > div.st-bc.st-dj.st-dl.st-dm.st-dn.st-b4.st-co.st-do.st-bd.st-cc.st-cd.st-dp.st-db")

pain.click()

asymp = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[3]/div/div/div/ul/div/div/li[4]')

asymp.click()

bp = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(6) > div > div.css-1nnn0hm.e1jwn65y0 > div.st-bc.st-b4.st-bd.st-b7.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b2.st-bn.st-av.st-ay.st-bo.st-bp.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw > div > input")

bp.send_keys(170)

chol = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(7) > div > div.css-1nnn0hm.e1jwn65y0 > div.st-bc.st-b4.st-bd.st-b7.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b2.st-bn.st-av.st-ay.st-bo.st-bp.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw > div > input")

chol.send_keys(203)

bs = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(8) > div > div > label:nth-child(1) > div.st-co.st-cs.st-ct.st-cu.st-cv.st-cw.st-az.st-b4.st-cx.st-cy.st-cz.st-d0.st-d1.st-d2.st-c8.st-d3.st-d4.st-d5.st-b2.st-bn")

bs.click()

ecg = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(9) > div > div > div > div.st-bc.st-dj.st-dl.st-dm.st-dn.st-b4.st-co.st-do.st-bd.st-cc.st-cd.st-dp.st-db")

ecg.click()

hyperventry = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[3]/div/div/div/ul/div/div/li[2]/span')

hyperventry.click()

hr = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(10) > div > div.css-1nnn0hm.e1jwn65y0 > div.st-bc.st-b4.st-bd.st-b7.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b2.st-bn.st-av.st-ay.st-bo.st-bp.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw > div > input")

hr.send_keys(108)

exang = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(11) > div > div > label:nth-child(2) > div.st-co.st-df.st-ct.st-cu.st-cv.st-cw.st-az.st-b4.st-cx.st-cy.st-cz.st-d0.st-d1.st-d2.st-c8.st-d3.st-d4.st-d5.st-b2.st-bn > div")

exang.click()

old = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(12) > div > div.css-1nnn0hm.e1jwn65y0 > div.st-bc.st-b4.st-bd.st-b7.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b2.st-bn.st-av.st-ay.st-bo.st-bp.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw > div > input")

old.click()

old.send_keys(Keys.HOME)

for x in range(6):
    old.send_keys(Keys.DELETE)
    
old.send_keys('0')

slope = driver.find_element_by_css_selector("#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(13) > div > div > div > div.st-bc.st-dj.st-dl.st-dm.st-dn.st-b4.st-co.st-do.st-bd.st-cc.st-cd.st-dp.st-db")

slope.click()

plana = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[3]/div/div/div/ul/div/div/li[2]')

plana.click()