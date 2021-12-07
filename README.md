# python-scrapping
This project was created using Python technology and flask tools to scrape a music site 

You need to install the following packages to get started :

 1 - pip install requests
 
 2 - pip install flask
 
 3 - pip install BeautifulSoup
 
Now just run the following command :

  python scrape.py
 
-----------------------------------------------
Search Music :
---

Method : GET

Action : /search

Parameter : q

Description : Returns list of searched music

----------------------------------------------
New Music :
---

Method : GET

Action : /new

Parameter : None

Description : Returns list of new music

----------------------------------------------
Get Music :
---

Method : GET

Action : /getmusic

Parameter : link

Description : Retrieve a Music by link

----------------------------------------------
Get Categories :
---

Method : GET

Action : /categories

Parameter : None

Description : Returns list of categories

----------------------------------------------
Get All Music a Category :
---

Method : GET

Action : /getcategories

Parameter : link

Description : Returns list of All music a specific category

----------------------------------------------

