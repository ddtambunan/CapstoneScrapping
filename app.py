from flask import Flask, render_template 
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from io import BytesIO
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def scrap(url):
    #This is fuction for scrapping
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content,"html.parser")
    
    #Find the key to get the information
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    df.rename(columns=df.iloc[0], inplace = True)
    df.drop([0], inplace = True)

    df[['ASK','BID']]= df[['ASK','BID']].astype('float')
    df['ASK'] = df['ASK']/100
    df['BID'] = df['BID']/100
    
   #end of data wranggling

    return df

@app.route("/")
def index():
    df = scrap('https://monexnews.com/kurs-valuta-asing.htm?kurs=JPY&searchdatefrom=01-01-2019&searchdateto=31-12-2019') #insert url here

    #This part for rendering matplotlib
    fig = plt.figure(figsize=(5,2),dpi=300) #tempat resize grafik
    df.plot.line() #tempat ganti jenis grafik dan settingnya
    
    #Do not change this part
    plt.savefig('plot1',bbox_inches="tight") 
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    #This part for rendering matplotlib

    #this is for rendering the table
    df = df.to_html(classes=["table table-bordered table-striped table-dark table-condensed"]) #cari di bootstrapt

    return render_template("index.html", table=df, result=result)


if __name__ == "__main__": 
    app.run()
