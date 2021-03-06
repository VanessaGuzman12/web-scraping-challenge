from splinter import Browser
from bs4 import BeautifulSoup as soup
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pymongo


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser=  Browser('chrome', **executable_path, headless=True)

    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    news_soup = soup(html, "html.parser")

    news_title = news_soup.find('div', class_="content_title").text

    news_p = news_soup.find('div', class_= 'article_teaser_body').text
    

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    images_soup = soup(html, "html.parser")

    images = images_soup.find_all('img', class_='headerimage fade-in')
    for img in images:
        if img.has_attr('src'):
            
            image=img['src']

    featured_image_url =  f'https://spaceimages-mars.com/{image}'
    


    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    hemisphere_soup = soup(html, "html.parser")

    hemis_html = hemisphere_soup.find_all('a',class_="itemLink product-item")

    hemis=[]
    for x in hemis_html:
        if x.has_attr('href'):
            hemis.append(x['href'])
            
    hemis_links =[]
    for x in hemis:
        if x not in hemis_links:
            hemis_links.append(x)

    hemis_links = hemis_links[0:4]
 

    cerberus_html = url + hemis_links[0]
    schiap_html= url + hemis_links[1]
    syrtis_html = url + hemis_links [2]
    valles_html = url + hemis_links[3]
   


    browser.visit(cerberus_html)
    html = browser.html
    cerberus_soup = soup(html, "html.parser")

    cerberus_img = cerberus_soup.find_all('img', class_='wide-image')
    for img in cerberus_img:
        if img.has_attr('src'):
            cerb=img['src']

    cerberus_image_url =url + cerb
   

    browser.visit(schiap_html)
    html = browser.html
    schiap_soup = soup(html, "html.parser")

    schiap_img = schiap_soup.find_all('img', class_='wide-image')
    for img in schiap_img:
        if img.has_attr('src'):
            schi=img['src']

    schiap_image_url =url + schi
  

    browser.visit(syrtis_html)
    html = browser.html
    syrtis_soup = soup(html, "html.parser")

    syrtis_img = syrtis_soup.find_all('img', class_='wide-image')
    for img in syrtis_img:
        if img.has_attr('src'):
            syrt=img['src']

    syrtis_image_url =url + syrt
  

    browser.visit(valles_html)
    html = browser.html
    valles_soup = soup(html, "html.parser")

    valles_img = valles_soup.find_all('img', class_='wide-image')
    for img in valles_img:
        if img.has_attr('src'):
            valles=img['src']

    valles_image_url =url + valles
    

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_image_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_image_url},
        {"title": "Schiaparelli Hemisphere", "img_url": schiap_image_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_image_url},
    ]
    

    url_mars = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url_mars)[0]

    tables.columns=['Description', 'Mars', 'Earth']
    tables.set_index('Description', inplace=True)

    html_table = tables.to_html()
    
  


    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_table": html_table    ,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    browser.quit()

    return mars_data

#print(scrape())
