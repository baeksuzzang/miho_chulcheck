import pickle
import glob
import tkinter
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

wait_time = 4
oneshin_url = 'https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&lang=ko-kr&bbs_theme=light&bbs_theme_device=1'
train_url = 'https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&utm_campaign=checkin&utm_id=6&lang=ko-kr&bbs_theme=light&bbs_theme_device=1'
bong3_url = 'https://act.hoyolab.com/bbs/event/signin-bh3/index.html?act_id=e202110291205111&utm_source=hoyolab&utm_medium=tools&bbs_theme=light&bbs_theme_device=1'
mihae_url = 'https://act.hoyolab.com/bbs/event/signin/nxx/index.html?act_id=e202202281857121&bbs_presentation_style=fullscreen&bbs_auth_required=true&utm_source=hoyolab&utm_medium=tools&lang=ko-kr&bbs_theme=light&bbs_theme_device=1'

class ChulCheck:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(oneshin_url)
        
    def add_cookies(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
    
    def refresh(self):
        self.driver.refresh()
        time.sleep(wait_time)
        
    def oneshin_check(self):
        self.driver.get(oneshin_url)
        time.sleep(wait_time)
        try:
            self.driver.find_element_by_css_selector('body > div._1NVi6w4R.custom-mihoyo-common-mask > div > div > span').click()
        except:
            pass
        time.sleep(wait_time)
        day = int(self.driver.find_element_by_css_selector('body > div.components-home-assets-__home_---home-page---C1pMbL.home-page > div.components-home-assets-__home_---home-content---1hcp1A > div:nth-child(1) > div > div > div.components-home-assets-__sign-content_---sign-header---A4aS9J > div.components-home-assets-__sign-content_---header-left---1o2pTm > div.components-home-assets-__sign-content_---day---1rVnsL.day > span').text)+1
        self.driver.find_element_by_css_selector('body > div.components-home-assets-__home_---home-page---C1pMbL.home-page > div.components-home-assets-__home_---home-content---1hcp1A > div:nth-child(1) > div > div > div.components-home-assets-__sign-content_---sign-list---1E-cUZ > div:nth-child({0})'.format(day)).click()
        
    def train_check(self):
        self.driver.get(train_url)
        time.sleep(wait_time)
        try:
            self.driver.find_element_by_css_selector('body > div.m-modal.m-dialog.components-pc-assets-__dialog_---common-dialog---MuR1Sk.components-pc-assets-__dialog_---common-dialog-sea---1XveKg > div.m-dialog-wrapper > div.m-dialog-footer > div').click()
        except:
            pass
        time.sleep(wait_time)
        day = int(self.driver.find_element_by_css_selector('body > div.components-pc-assets-__home_---home-page---2m-8BR.home-page > div.components-pc-assets-__home_---scroller---ZF2lsm > div.components-pc-assets-__main-module_---main-module---3jY8-Z > div.components-pc-assets-__main-module_---content---1ah-Ie > div.components-pc-assets-__main-module_---header---3hMHBC.components-pc-assets-__main-module_---header-sea---1D_UPV > div:nth-child(1) > p.components-pc-assets-__main-module_---day---3Q5I5A.day > span').text)+1
        self.driver.find_element_by_css_selector('body > div.components-pc-assets-__home_---home-page---2m-8BR.home-page > div.components-pc-assets-__home_---scroller---ZF2lsm > div.components-pc-assets-__main-module_---main-module---3jY8-Z > div.components-pc-assets-__main-module_---content---1ah-Ie > div.components-pc-assets-__prize-list_---prize-list---3s4FAb.components-pc-assets-__prize-list_---prize-list-sea---3CblUM > div.components-pc-assets-__prize-list_---list---26M_YG > div:nth-child({0})'.format(day)).click()
        
    def bong3_check(self):
        self.driver.get(bong3_url)
        time.sleep(wait_time)
        day = int(self.driver.find_element_by_css_selector('body > div.components-home-assets-__home_---home-page---C1pMbL.home-page > div.components-home-assets-__home_---content---MDDVqg.home-content > div > div.components-home-assets-__sign-content_---list---3L0nzm > div.components-home-assets-__sign-content_---message---2QQyLs > div.components-home-assets-__sign-content_---sginInfo---1JJiAg > div.components-home-assets-__sign-content_---sginInfo__text---1T7GkB > div > span').text)+1
        self.driver.find_element_by_css_selector('body > div.components-home-assets-__home_---home-page---C1pMbL.home-page > div.components-home-assets-__home_---content---MDDVqg.home-content > div > div.components-home-assets-__sign-content_---list---3L0nzm > div.swiper-container.components-home-assets-__sign-content_---mySwiper---2d-HzX.swiper-container-horizontal > div > div.swiper-slide.swiper-slide-active > div > div:nth-child({0})'.format(day)).click()
        
    def mihae_check(self):
        self.driver.get(mihae_url)
        time.sleep(wait_time)
        day = int(self.driver.find_element_by_css_selector('body > div.components-pc-assets-__home_---home-page---2m-8BR.home-page > div.components-pc-assets-__home_---scroller---ZF2lsm > div.components-pc-assets-__main-module_---main-module---3jY8-Z > div.components-pc-assets-__main-module_---content---1ah-Ie > div.components-pc-assets-__main-module_---header---3hMHBC > p.components-pc-assets-__main-module_---day---3Q5I5A.day > span').text)+1
        self.driver.find_element_by_css_selector('body > div.components-pc-assets-__home_---home-page---2m-8BR.home-page > div.components-pc-assets-__home_---scroller---ZF2lsm > div.components-pc-assets-__main-module_---main-module---3jY8-Z > div.components-pc-assets-__main-module_---content---1ah-Ie > div.components-pc-assets-__prize-list_---prize-list---3s4FAb > div.components-pc-assets-__prize-list_---list---26M_YG > div:nth-child({0})'.format(day)).click()

def check_cookies():
    if glob.glob('cookies.pkl'):
        return True
    else:
        return False

def get_cookies():
    def login_complete():
        pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
        window.destroy()
        driver.quit()
        
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(oneshin_url)

    window=tkinter.Tk()
    window.title("크롬 로그인 완료 후 확인버튼")
    window.geometry("350x100+100+100")
    window.resizable(False, False)
    label = tkinter.Label(window, text='로그인 후 크롬창을 켠 채로 쿠키저장을 눌러주세요!')
    label.pack()
    btn = tkinter.Button(width = 30 , text = '쿠키 저장', command = login_complete)
    btn.pack()
    window.lift()
    window.mainloop()

def main():
    if check_cookies():
        f = ChulCheck()
        f.add_cookies()
        f.refresh()
        f.oneshin_check()
        f.train_check()
        f.bong3_check()
        f.mihae_check()
    else:
        get_cookies()

if __name__ == "__main__":
    main()