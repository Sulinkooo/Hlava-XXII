#!/usr/bin/env python3

'''
# Tento skript uploaduje Ulice cez webrozhranie (FF) lebo remoteuplad je odstaveny
'''

import time, os, sys, subprocess, datetime
import selenium
from selenium import webdriver
from time import gmtime, strftime

## Get profile class
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
## get the Firefox profile object
firefoxProfile = FirefoxProfile()
## Disable CSS
firefoxProfile.set_preference('permissions.default.stylesheet', 2)

try:

    with open('ulice-skript.txt', 'a') as zapis:
        zapis.write(strftime('%Y-%m-%d %H:%M:%S: ', gmtime()))
        zapis.write('... spustil sa skript pre noremote-Ulice .... \n')

    nazov = "Ulice"
    nazov2 = "Ordinace v ruzove zahrade"
    nazov3 = "Modry kod"

    torrent_name = sys.argv[2]#'Ulice 3252.avi' #sys.argv[2]
    torrent_path = sys.argv[3]#'/home/suli/subory/Serial' #sys.argv[3]

    mmm = torrent_name
    ppp = torrent_path

    meno = torrent_name
    fn = torrent_path+'/'+torrent_name
    tn = 'teraz som si vymyslel kokotinu...'

    with open('ulice-skript.txt', 'a') as zapis:
        zapis.write(strftime("%Y-%m-%d %H:%M:%S: ", gmtime()))
        zapis.write('UliceSkript nacitalo info z Deluge\n\n')
except:
    print('Kokot Rebekin')

try:
    if nazov in torrent_name:


        
        #torrent_name = torrent_name.replace(' ','')    # najprv odstrani vsetky medzery
        torrent_name = torrent_name.replace('-',' ')    # potom pomlcky nahradi medzerami
        torrent_name = torrent_name.replace('_',' ')    # potom podtrzniky nahradi medzerami
        torrent_name = torrent_name.replace('   ',' ')  # potom trojitu medzeru nahradi medzerou
        torrent_name = torrent_name.replace('  ',' ')   # potom dvojitu medzeru nahradi medzerou
        torrent_name = torrent_name.replace(' . ',' ')
        torrent_name = torrent_name.replace('..',' ')

        tn = torrent_path+"/"+meno # tn = torrent name
        fn = torrent_path+"/"+torrent_name[:-4]+" CZ Dabing FullHD 1080p.avi"# fn = finalny nazov *** [:-4] rez polom - odsekne posledne 4 znaky. Tj.: .avi

        fn = fn.replace('   ',' ')
        fn = fn.replace('  ',' ')

        subprocess.call(['ffmpeg', '-i', tn, '-s', '1920x1080', '-b', '6000k', fn])
        
        odkaz = 'http://194.88.107.193/subory/Serial/' + fn[--25:]

        # nepis to ako kokot, co takto jedna premenna, string obsahujuca vsetko? ?? :)
        # vypis = 'popisok: \n'+'ina kokotina \n\n'+cas+'dalsia kokotina'
        # f.write(vypis) 
    
        with open('ulice-skript.txt', 'a') as f:
            f.write(strftime('%Y-%m-%d %H:%M:%S: ', gmtime()))
            f.write('SUBPROCESS\ndalsie Ulice stiahnute a prekodovane do 1080p 6000k bitrate...\nLink: ')
            f.write(odkaz)
            f.write('\n')
            f.write(torrent_name)
            f.write('\n')
            f.write(tn)
            f.write('\n')
            f.write(fn)
            f.write('\n')

        driver = webdriver.Firefox(firefoxProfile)
        driver.get('https://prehraj.to/profil/nahrat-soubor/')
        time.sleep(2)

        driver.find_element_by_name('email').send_keys('adresanaregistracie@gmail.com')
        driver.find_element_by_name('password').send_keys('Hesloakoziadneine!')
        driver.find_element_by_xpath('//*[@id="frm-login-loginForm"]/fieldset/div[3]/div/button').click()
        time.sleep(5)
        
        menoUploadSuboru = fn
        element = driver.find_element_by_id('fileupload')
        
        for i in range(0, 17):
            driver.find_element_by_id('fileupload').send_keys(menoUploadSuboru)
            element.clear()

        driver.find_element_by_id('confirm-checkbox').click()
        time.sleep(2)

        driver.find_element_by_id('upload').click()

        while True:
            try:
                driver.find_element_by_id('to-files').click()
                print('Koniec uploadovania')
                driver.quit()
                break
            except:
                print('skusil som znova overit stav uploadu...')
                time.sleep(5)

    elif nazov2 in torrent_name or nazov3 in torrent_name:
        driver = webdriver.Firefox(firefoxProfile)
        driver.get('https://prehraj.to/profil/nahrat-soubor/')
        time.sleep(2)

        driver.find_element_by_name('email').send_keys('adresanaregistracie@gmail.com')
        driver.find_element_by_name('password').send_keys('Hesloakoziadneine!')
        driver.find_element_by_xpath('//*[@id="frm-login-loginForm"]/fieldset/div[3]/div/button').click()
        time.sleep(5)
        
        menoUploadSuboru = fn
        element = driver.find_element_by_id('fileupload')
        
        for i in range(0, 7):
            driver.find_element_by_id('fileupload').send_keys(menoUploadSuboru)
            element.clear()

        driver.find_element_by_id('confirm-checkbox').click()
        time.sleep(2)

        driver.find_element_by_id('upload').click()

        while True:
            try:
                driver.find_element_by_id('to-files').click()
                print('Koniec uploadovania')
                driver.quit()
                break
            except:
                print('skusil som znova overit stav uploadu...')
                time.sleep(5)

    elif 'Film' in torrent_path:
        zoznam = torrent_name.split('.')

        pozicia = 0

        for rok in zoznam:
            try:
                int(rok) # toto asi mozem vynechat ???
                if int(rok) > 1900 and int(rok) < 2100:
                    print('Rok vyroy je:', rok, 'a tato hodnota je na pozicii: ', pozicia)
                    spinavyNazovFilmu = '.'.join(zoznam[0:pozicia])
                    print('spinavy nazov filmu je:', spinavyNazovFilmu)
                    cistyNazovFilmu = ' '.join(zoznam[0:pozicia])
                    print('spinavy nazov filmu je:', cistyNazovFilmu)
                    break
            except:
                pozicia += 1
                #print(pozicia)
    
        pozicia = 0
        for kvalita in zoznam:
            try:
                if kvalita in ('720','720p','1080','1080p','mHD','HD','FullHD','FULLHD','FHD','XviD'):
                    print('kvalita videa je:', kvalita)
                    break
            except:
                pozicia += 1

        driver = webdriver.Firefox(firefoxProfile)
    
        driver.get('https://www.csfd.cz/hledat/?q='+cistyNazovFilmu)

        for li in range(1, 5):
            li = str(li)
            xpathDetail = '//*[@id="search-films"]/div[1]/ul[1]/li['+li+']/div/p[1]'
            
            #                                      //*[@id="search-films"]/div[1]/ul[1]/li[2]/div/p[1] ... 4 na stranke
            detail = driver.find_element_by_xpath(xpathDetail).text
            detailDetail = detail.split(', ')
            zanerFilmu = detailDetail[0]
            krajinaPovodu = detailDetail[1]
            rokVyroby = int(detailDetail[2])
            
            print('detail:', detail, '\ndetailDetail:', detailDetail, '\nzanerFilmu:', zanerFilmu, '\nkrajinaPovodu:', krajinaPovodu, '\nrokVyroby', rokVyroby, '\n')
            
            print(type(rokVyroby))
            print(rok)
            print(type(rok))
            print(rok, type(rok), type(int(rok)))
            
            
            if int(rokVyroby) == int(rok):
                #                             //*[@id="search-films"]/div[1]/ul[1]/li[2]/div/h3/a .... 4 na stranke
                driver.find_element_by_xpath('//*[@id="search-films"]/div[1]/ul[1]/li['+li+']/div/h3/a').click()
                time.sleep(5)
                
                filmik = driver.find_element_by_xpath('//*[@id="profile"]/div[1]/div[2]/div[1]/h1').text
                print('aneb by xpath a .getText() sme dospeli k:', filmik)
                
                break
            else:
                continue
        
        
        
        
        #driver.quit()
        
        if kvalita == 'mHD':
            kvalita = 'mHD 720p'
        
        if 'XviD' in torrent_name:
            koncovka = '.avi'
        else:
            koncovka = '.mkv'

        finalNazovFilmu = filmik+' CZ Dabing '+kvalita+' '+str(rok)+' MSDos'+koncovka
        print(torrent_name)
        print(finalNazovFilmu)

        try:
            if os.path.exists('/home/suli/subory/Film-P/'+filmik) is False:
                print('Zlozka neexistovala, vytvaram zlozku:', filmik, 'v /home/suli/subory/Film-P')
                os.mkdir('/home/suli/subory/Film-P/'+filmik)
                print('Zlozka vytvorena...')

            if os.path.exists('/home/suli/subory/Film-P/'+filmik) is True:
                print('zlozka existuje, vytvaram symlink...')
                if 'Xvid' in torrent_name:
                    zdroj = torrent_path+'/'+torrent_name+'/'+torrent_name+'.avi'
                    ciel = '/home/suli/subory/Film-P/'+filmik+'/'+finalNazovFilmu
                    os.symlink(zdroj, ciel)
                    
                    #driver = webdriver.Firefox(firefoxProfile)
                    driver.get('https://prehraj.to/profil/nahrat-soubor/')
                    time.sleep(2)
                    
                    driver.find_element_by_name('email').send_keys('adresanaregistracie@gmail.com')
                    driver.find_element_by_name('password').send_keys('Hesloakoziadneine!')
                    driver.find_element_by_xpath('//*[@id="frm-login-loginForm"]/fieldset/div[3]/div/button').click()
                    time.sleep(5)
                    
                    menoUploadSuboru = ciel
                    element = driver.find_element_by_id('fileupload')
                    
                    for i in range(0, 4):
                        driver.find_element_by_id('fileupload').send_keys(menoUploadSuboru)
                        element.clear()
                    
                    driver.find_element_by_id('confirm-checkbox').click()
                    time.sleep(2)
                    
                    driver.find_element_by_id('upload').click()
                    
                    while True:
                        try:
                            driver.find_element_by_id('to-files').click()
                            print('Koniec uploadovania')
                            driver.quit()
                            break
                        except:
                            print('skusil som znova overit stav uploadu...')
                            time.sleep(5)
                else:
                    zdroj = torrent_path+'/'+torrent_name+'/'+torrent_name+'.mkv'
                    ciel = '/home/suli/subory/Film-P/'+filmik+'/'+finalNazovFilmu
                    os.symlink(zdroj, ciel)
                    driver.get('https://prehraj.to/profil/nahrat-soubor/')
                    time.sleep(2)
                    
                    driver.find_element_by_name('email').send_keys('adresanaregistracie@gmail.com')
                    driver.find_element_by_name('password').send_keys('Hesloakoziadneine!')
                    driver.find_element_by_xpath('//*[@id="frm-login-loginForm"]/fieldset/div[3]/div/button').click()
                    time.sleep(5)
                    
                    menoUploadSuboru = ciel
                    element = driver.find_element_by_id('fileupload')
                    
                    for i in range(0, 4):
                        driver.find_element_by_id('fileupload').send_keys(menoUploadSuboru)
                        element.clear()
                    
                    driver.find_element_by_id('confirm-checkbox').click()
                    time.sleep(2)
                    
                    driver.find_element_by_id('upload').click()
                    
                    while True:
                        try:
                            driver.find_element_by_id('to-files').click()
                            print('Koniec uploadovania')
                            driver.quit()
                            break
                        except:
                            print('skusil som znova overit stav uploadu...')
                            time.sleep(5)
        except Exception as exception:
            print(exception.__class__.__name__, ':' , str(exception))
            print('halo')

    else:
        with open('ulice-skript.txt', 'a') as f:
            f.write(strftime('%Y-%m-%d %H:%M:%S: ', gmtime()))
            f.write('BTW mimo ineho som zatial stiahol: ')
            f.write(torrent_name)
            f.write('\n')


except Exception as exception:
    with open('ulice-skript.txt', 'a') as chyba:
        chyba.write(strftime('%Y-%m-%d %H:%M:%S: ', gmtime()))
        obsahChyby = str(exception)
        chyba.write('KURVAAAAAAAA CHYBAAAAAAAAAA !!!!!!!!! \n\n')
        chyba.write(exception.__class__.__name__)
        chyba.write(': ')
        chyba.write(obsahChyby)
        chyba.write('\n\n\n\n')
    
