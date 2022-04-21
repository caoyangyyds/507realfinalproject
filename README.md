Caoyang Shen
Project code:
https://github.com/caoyangyyds/507finalproject/blob/main/song_dict.json
https://github.com/caoyangyyds/507finalproject/blob/main/datafetch.py

Data source:
a.	Billboard 2021 top 100 singers.
Url: https://www.billboard.com/charts/year-end/top-artists/
Formats: HTML
Methods: I scrape the data from the website through BeautifulSoup
Summary data: 100-120 records available, and 100 records retrieved. I want to find the top 100 singer’s name, and put them into a list.
b.	Spotify top ten songs of singers in top 100 and the songs’ features.
Url:  
Formats: Json
Methods: I used Spotipy.oauth2 to get the data.
Summary data: Trillions of data are available, and I retrieve 1000 records (100 singers with 10 top songs).
Evidence of caching
 

Data structure:
I use tree to save the data. The rank of the singer will be the key of the tree, and the information of the singer will be the information. Once inputting a number, the system will give the information of the certain singer.


Interaction and Presentation Plans：
First, the users will be asked which singer they want to see in this top 100 list, and they choose one or a range. In the Flask home page, I will show the result of the singer/singers. After then, I will ask which singer you want to see his/her/their detail information. In the Flask/detail page, I will present a table including this singer’s top ten songs with the danceability, energy and tempo information.

Demo link: https://youtu.be/FfhzuUEUZlQ
