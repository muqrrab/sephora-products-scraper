
from django.http import HttpResponse
from django.shortcuts import render

from django.db.models import Count
# Create your views here.

from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from openpyxl import load_workbook
import random
from .models import Product,AllLinks,SingleLinks,LinktoObtain,ShortProduct

def scrape(request):

    a = 0
    grouplist = []
    subgroup1list = []
    subgroup2list = []
    brandlist = []
    namelist = []
    pricelist = []
    ingredientlist = []
    productlinklist = []
    linklist = []


    user_agents_list = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36'    ]

    options = webdriver.ChromeOptions()

    # options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--user-agent="'+random.choice(user_agents_list)+'"')
    options.add_argument("--accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
    options.add_argument("--accept-language=en-US,en;q=0.9")
    options.add_argument("--accept-encoding=gzip, deflate, br")
    options.add_argument("--connection=keep-alive")
    options.add_argument("--upgrade-insecure-Requests=1")
    options.add_argument("--sec-fetch-dest=document")
    options.add_argument("--sec-fetch-mode=navigate")
    options.add_argument("--sec-fetch-site=none")
    options.add_argument("--sec-fetch-user=?1")

    s = Service('C:/Chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=s,options=options)

    # driver.get("https://www.sephora.com/shop/moisturizing-cream-oils-mists")

    # try:
    #     wait = WebDriverWait(driver, 8)
    #     wait.until(ec.visibility_of_element_located((By.XPATH,"//button[@aria-label='Continue shopping']")))
    #     driver.find_element((By.XPATH,"//button[@aria-label='Continue shopping']")).click()
    # except:
    #     pass

    allp = Product.objects.all()
    alll = LinktoObtain.objects.all()

    # return HttpResponse('ok')
    # book = load_workbook('MoisturesLinks.xlsx')
    # sheet = book.active

    # rows = sheet.rows
    # for r in rows:
    #     for cell in r:
    #         linklist.append(cell.value)

    print('Enter success')
    check2 = True

    for link in alll:
        check=True

        # if check2:
        #     for l in allp:
        #         if link.link == l.link:
        #             check=False
        #             print(str(a)+' Link skipped')
        #     a+=1
        
        if check:
            # check2=False
            # driver.implicitly_wait(2)
            
            driver.get(link.link)

            try:
                wait = WebDriverWait(driver, 0.5)
                wait.until(ec.visibility_of_element_located((By.XPATH,"//button[@aria-label='Continue shopping']")))
                try:
                    driver.find_element(By.XPATH,"//button[@aria-label='Continue shopping']").click()
                except:
                    pass
            except:
                pass

            # sleep(random.uniform(0.4, 0.6))
            print(f'\n\n\nEnter to product section{a}')
            try:
                group = driver.find_element(By.XPATH,"//nav[@aria-label='Breadcrumb']//li[1]").text
            except:
                group='None Found'
            try:
                subgroup1 = driver.find_element(By.XPATH,"//nav[@aria-label='Breadcrumb']//li[2]").text
            except:
                subgroup1='None Found'
            try:
                subgroup2 = driver.find_element(By.XPATH,"//nav[@aria-label='Breadcrumb']//li[3]").text
            except:
                subgroup2='None Found'
            try:
                brand = driver.find_element(By.XPATH,"//h1[@class='css-11zrkxf e65zztl0']/a").text
            except:
                brand='None Found'
            try:                
                name = driver.find_element(By.XPATH,"//h1[@class='css-11zrkxf e65zztl0']/span").text
            except:
                name='None Found'
            try:
                price = driver.find_element(By.XPATH,"(//span[@class='css-18jtttk'])[1]").text
            except:
                price='None Found'
            sleep(random.uniform(0.1,0.2))

            # wait = WebDriverWait(driver,1)
            # wait.until(ec.element_to_be_clickable((By.XPATH,"//button[@data-at='ingredients']")))
            try:
                driver.find_element(By.XPATH,"(//button[@data-at='ingredients'])[1]").click()
                sleep(random.uniform(0.1, 0.2))
                ingredient = driver.find_element(By.XPATH,"//div[@id='ingredients']//div[@class='css-1ue8dmw eanm77i0']/div").text
            except:
                ingredient = 'None Found'

            Product.objects.filter(link=link.link).update(
                group=group,
                subgroup1=subgroup1,
                subgroup2=subgroup2,
                brand=brand,
                name=name,
                price=price,
                ingredient=ingredient
            )
            # print('Object Created '+str(a))
            print('Object Updated '+str(a))
            if ingredient == '':
                print('No ingredient')

            # out = open('check.txt','a')
            # out.write(str(a)+')\t'+group+'\t'+subgroup1+'\t'+subgroup2+'\t'+brand+'\t'+name+'\t'+price+'\t'+ingredient+'\n')
            a+=1


    





    return HttpResponse('Ok')


def link(request):
    user_agents_list = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36'    ]

    options = webdriver.ChromeOptions()

    # options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--user-agent="'+random.choice(user_agents_list)+'"')
    options.add_argument("--accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
    options.add_argument("--accept-language=en-US,en;q=0.9")
    options.add_argument("--accept-encoding=gzip, deflate, br")
    options.add_argument("--connection=keep-alive")
    options.add_argument("--upgrade-insecure-Requests=1")
    options.add_argument("--sec-fetch-dest=document")
    options.add_argument("--sec-fetch-mode=navigate")
    options.add_argument("--sec-fetch-site=none")
    options.add_argument("--sec-fetch-user=?1")

    s = Service('C:/Chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(service=s,options=options)

    url = [
        'https://www.sephora.com/shop/cleanser',
        'https://www.sephora.com/shop/facial-treatments',
        'https://www.sephora.com/shop/face-mask',
        'https://www.sephora.com/shop/eye-treatment-dark-circle-treatment',
        'https://www.sephora.com/shop/lip-balm-lip-care',
        'https://www.sephora.com/shop/sunscreen-sun-protection',
        'https://www.sephora.com/shop/self-tanning-products',
        'https://www.sephora.com/shop/skin-care-tools',
        'https://www.sephora.com/shop/wellness-skincare',
        'https://www.sephora.com/shop/skin-care-solutions',
        'https://www.sephora.com/shop/vegan-skin-care',
        'https://www.sephora.com/shop/skin-care-sets-travel-value',
        'https://www.sephora.com/shop/mini-skincare'
    ]

    for u in url:
        print(u)
        driver.get(u)

        try:
            wait = WebDriverWait(driver, 2)
            wait.until(ec.visibility_of_element_located((By.XPATH,"//button[@aria-label='Continue shopping']")))
            driver.find_element((By.XPATH,"//button[@aria-label='Continue shopping']")).click()
        except:
            pass

        sleep(random.uniform(0.2, 0.8))

        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(random.uniform(0.1, 0.5))
        driver.refresh()
        while True:
            total_height = int(driver.execute_script("return document.body.scrollHeight"))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            sleep(random.uniform(0.1, 0.5))
        
            try:
                wait = WebDriverWait(driver, 3)
                wait.until(ec.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Show More Products']")))
                driver.find_element(By.XPATH,"//button[normalize-space()='Show More Products']").click()
                sleep(random.uniform(3.1, 3.9))
            except:
                total_height = int(driver.execute_script("return document.body.scrollHeight"))
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                for i in range(1, total_height, 25):
                    driver.execute_script(f"window.scrollTo(0, {i});")
                sleep(10)
                break
        
        
        link = driver.find_elements(By.XPATH,"(//a[@class='css-klx76'])")
        name = driver.find_elements(By.XPATH,"//span[@class='ProductTile-name css-h8cc3p eanm77i0']")
        subgroup = driver.find_element(By.XPATH,"//div[@class='css-1lij8wv']//li[2]/span").text
        


        
        linklist = []
        namelist = []

        check = True

        for l in link:
            href = l.get_attribute('href')
            linklist.append(href)
        
        for n in name:
            namelist.append(n.text)

        lenth = 0
        if len(linklist) < len(namelist):
            lenth = len(linklist)
        elif len(linklist) > len(namelist):
            lenth = len(namelist)
        else:
            lenth = len(linklist)

        for i in range(lenth):
            ShortProduct.objects.create(
                    group = 'Skin Care',
                    subgroup = subgroup,
                    name = namelist[i],
                    link=linklist[i]
            )


        print("Link saved")
        print(len(linklist))

    return HttpResponse('Ok')
    
def dels(request):


    a=0

    g=[]
    sg=[]
    n=[]
    l=[]

    pro = ShortProduct.objects.all()

    for p in pro:
        g.append(p.group)
        sg.append(p.subgroup)
        n.append(p.name)
        l.append(p.link)
    
    '''
    p = AllLinks.objects.all()


    p = AllLinks.objects.raw('SELECT id,link, COUNT(*) AS "Count" FROM scraper_alllinks  GROUP BY link ORDER BY Count(*) DESC')

    for i in p:
        #non-duplicate
        if i.Count == 1:
            a+=i.Count
        if i.Count > 1:
            a+=1


        if i.Count == 2:
            b+=1
        elif i.Count == 3:
            c+=2
        elif i.Count == 4:
            d+=3
        elif i.Count == 5:
            e+=4
        elif i.Count == 6:
            f+=5
            
'''




    '''
    duplicates = AllLinks.objects.values(
    'link'
    ).annotate(link_count=Count('link')).filter(link_count__gt=1)

    records = AllLinks.objects.filter(link__in=[item['link'] for item in duplicates])
'''



    # print([item.id for item in records])
    # for i in l:
    #     LinktoObtain.objects.create(link=i.link)

    
    

    # for row in p.reverse():
    #     if AllLinks.objects.filter(link=row.link).count() == 2:
    #         linklist.append(row.link)
    #         a += 1
    #     elif AllLinks.objects.filter(link=row.link).count() == 3:
    #         b  += 1
    #     elif AllLinks.objects.filter(link=row.link).count() == 4:
    #         c  += 1
    #     elif AllLinks.objects.filter(link=row.link).count() == 5:
    #         d  += 1
    #     elif AllLinks.objects.filter(link=row.link).count() == 6:
    #         e  += 1
    #     elif AllLinks.objects.filter(link=row.link).count() == 7:
    #         f  += 1
    #     elif AllLinks.objects.filter(link=row.link).count() == 1:
    #         g  += 1


    data = pd.DataFrame(
        {
            'Category':g,
            'Sub Category':sg,
            'Product Name':n,
            'Link':l,
        }
    )

    data.to_excel('SkinCareCategories.xlsx', sheet_name='sheet1', index=False)

    print('Done')
    # a=str(a)+' '+str(b)+' '+str(c)+' '+str(d)+' '+str(e)+' '+str(f)
    # a = 'Two duplicate '+str(a)+'\nThree duplicate '+str(b)+\
    # '\nFour duplicate '+str(c)+'\nFive duplicate '+str(d)+'\nSix duplicate '+str(e)+'\nNo duplicates '+str(g)
    return HttpResponse(a)
