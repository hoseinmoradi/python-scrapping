import requests
import urllib.request
from flask import Flask, request
import time
import json
import jsonpickle
from json import JSONEncoder
from bs4 import BeautifulSoup
from collections import defaultdict
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
CORS(app, support_credentials=True)


#search music
@app.route('/search')
def searchMusic():
    search = request.args.get('q')
    return Music(search)
 
    
#new music
@app.route('/new')
def Music(result):
        if(not result):
            url = 'https://pop-music.ir/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            divs = soup.findAll(class_= 'leftc')
            all_new_music = list()
            for div in divs:
                index = list()
                title = div.select("header h2 a")
                image = div.select("p img")
                link = div.select("div.morelink a")
                
                if(title != []):
                    title = title[0].text
                    title = title.replace("دانلود","")
                    title = title.replace("جدید","")
            
                if(image != []):
                    final_image = image[0]['src']
                    
                if(link != []):
                    link = link[0]['href']
                    
                index.append({"title":title,"image":final_image,"link":link})
                all_new_music.append(index[0]) 
            print(all_new_music)
            return jsonify(all_new_music)
        else:
            urls = "https://pop-music.ir?blogs=1,5&s="+result
            response = requests.get(urls)
            soup = BeautifulSoup(response.text, "html.parser")
            divs = soup.findAll(class_= 'leftc')
            all_new_music = list()
            for div in divs:
                index = list()
                title = div.select("header h2 a")
                image = div.select("p img")
                link = div.select("div.morelink a")
                if(title != []):
                    title = title[0].text
                    title = title.replace("دانلود","")
                    title = title.replace("جدید","")
                
                if(image != []):
                    final_image = image[0]['src']
                
                if(link != []):
                    link = link[0]['href']
                
                index.append({"title":title,"image":final_image,"link":link})
                all_new_music.append(index[0]) 
            return jsonify(all_new_music)
    
#get track   
@app.route('/getmusic')
def ExtractMusic():  
    index = list()  
    link = request.args.get('link')
    response = requests.get("https://pop-music.ir/"+link)
    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find(class_= 'leftc') 
    title = divs.select("header h2 a")
    image = divs.select("p img")
    matter = divs.findAll("p")
    mp3 = soup.select("div[class=download] > p[class=downloader] > a")
    if(title != []):
        title = title[0].text
        title = title.replace("دانلود","")
        title = title.replace("جدید","")
    else:
        title = ""
    if(image != []):
        image = image[0]['src']
    music_text = ''
    for i in range(5,len(matter)):
            music_text  += matter[i].text + "\n"
    if(mp3 != []):
        mp3 = mp3[0]['href']
    index.append({'title':title,'image':image,'music_text':music_text,'mp3':mp3})
    return jsonify(index)
    

@app.route('/categories')
@cross_origin(supports_credentials=True)
def CategoryMusic():
    all_new_music = list()
    response = requests.get("https://pop-music.ir")
    soup = BeautifulSoup(response.text, "html.parser")
    cat = soup.findAll("li",{"class": "cat-item"})
    for index, item in enumerate(cat):
        if(index > 2):
            print(index)
            index = list()
            title = item.select("a")[0].text
            category = item.select("a")[0]["href"]
            index.append({"link":category,"title":title})
            all_new_music.append(index[0]) 
    return jsonify(all_new_music)

@app.route('/getcategories')
def GetCategories():
    link = request.args.get('link')
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.findAll(class_= 'leftc')
    all_new_music = list()
    for div in divs:
        index = list()
        title = div.select("header h2 a")
        if(title != []):
            title = title[0].text
            title = title.replace("دانلود","")
            title = title.replace("جدید","")
        image = div.select("p img")
        if(image != []):
            final_image = image[0]['src']
            print(image)
        
        link = div.select("div.morelink a")
        print(link)
        if(link != []):
            link = link[0]['href']
            print(link)
        index.append({"title":title,"image":final_image,"link":link})
        all_new_music.append(index[0]) 
            
    return jsonify(all_new_music)

  
if __name__ == '__main__':
    app.debug = True
    app.run()