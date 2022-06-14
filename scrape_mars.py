from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_p = mars_articles(browser)
    img_urls_titles = hemispheres_mars(browser)

    data = {
        'news_title' : news_title,
        'news_paragraph' : news_p,
        'featured_image' : mars_images(browser),
        'table' : tables_mars(),
        'hemispheres' : img_urls_titles
    }
    browser.quit()
    return data


def mars_articles():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser= Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find_all('div', class_="content_title")
    for title in news_title:
        news_title= title.text

    news_p = soup.find_all('div', class_= 'article_teaser_body')
    for paragraph in news_p:
        news_p = paragraph.text
    
    browser.quit()
    
    return news_title, news_p
    
    

def mars_images():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser= Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    images_soup = bs(html, "html.parser")

    images = images_soup.find_all('img', class_='headerimage fade-in')
    for img in images:
        if img.has_attr('src'):
            print(img['src'])
            image=img['src']

    featured_image_url =  f'https://spaceimages-mars.com/{image}'
    

    browser.quit ()
    return featured_image_url

def hemispheres_mars():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser= Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    hemisphere_soup = bs(html, "html.parser")

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
   


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser= Browser('chrome', **executable_path, headless=False)
    browser.visit(cerberus_html)
    html = browser.html
    cerberus_soup = bs(html, "html.parser")

    cerberus_img = cerberus_soup.find_all('img', class_='wide-image')
    for img in cerberus_img:
        if img.has_attr('src'):
            cerb=img['src']

    cerberus_image_url =url + cerb
   

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser= Browser('chrome', **executable_path, headless=False)
    browser.visit(schiap_html)
    html = browser.html
    schiap_soup = bs(html, "html.parser")

    schiap_img = schiap_soup.find_all('img', class_='wide-image')
    for img in schiap_img:
        if img.has_attr('src'):
            schi=img['src']

    schiap_image_url =url + schi
  

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser= Browser('chrome', **executable_path, headless=False)
    browser.visit(syrtis_html)
    html = browser.html
    syrtis_soup = bs(html, "html.parser")

    syrtis_img = syrtis_soup.find_all('img', class_='wide-image')
    for img in syrtis_img:
        if img.has_attr('src'):
            syrt=img['src']

    syrtis_image_url =url + syrt
  

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser= Browser('chrome', **executable_path, headless=False)
    browser.visit(valles_html)
    html = browser.html
    valles_soup = bs(html, "html.parser")

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
    

    browser.quit()
    return hemisphere_image_urls

def tables_mars():
    url_mars = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url_mars)

    comparison_df = tables[0]
    comparison_df = comparison_df.drop([0], axis = 0)

    cols = list(comparison_df.columns)
    cols[0] = "Mars - Earth Comparison"
    cols[1] = "Mars"
    cols[2]= "Earth"
    comparison_df.columns = cols

    df = comparison_df.reset_index(drop=True)

    html_table = df.to_html()
    html_table.replace('\n', '')
    print(html_table)


