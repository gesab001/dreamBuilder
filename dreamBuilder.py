import requests
import os
import sqlite3
import mysql.connector

def addHymnMYSQL(number, title, verses):
    mydb = mysql.connector.connect(
       host="bibledb.cvtfhbljhzkg.ap-southeast-2.rds.amazonaws.com",
       user="giovanni",
       passwd="mypassword",
       database="bible"
    )
    print(mydb) 

    mycursor = mydb.cursor()

    sql = "INSERT INTO HYMNS (NUMBER, TITLE, VERSES) VALUES (%s, %s, %s)"
    val = (number, title, verses)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, title, "successful")


def addHymn(number, title, verses):
        conn = sqlite3.connect('hymn2.db')
        conn.execute("INSERT INTO HYMNS (NUMBER, TITLE, VERSES) VALUES(?, ?, ?)", (number, title, verses));
        conn.commit()
        print (str(number) + " " + str(title) + "  added successfully");
        conn.close()    

response = requests.get('http://www.formypeople.org/dreams/')
dreamtitles = str(response.content) #get the raw website content
dreamtitles = dreamtitles.split('class="date">') #extract the date and title
del dreamtitles[155:]
del dreamtitles[3:81]
dreamtitles[::-1] #delete content at the end
 # delete content at the beginning
for title in dreamtitles[::-1]:
    if "formypeople.org/dream/" in title: # delete lines that don't contain a link to the dream
      index = dreamtitles.index(title)
      getDate = title.split(" - </span>  <a href=\"")      
      date = getDate[0] #the date of the dream
      link = getDate[1] # the link to the dream
      link = link[:link.index("</a></div>")]
      getName = link.split('">')
      dreamname = getName[1] #the name of the dream
      purelink = getName[0] # the complete link to the dream
      getDreamNumber = dreamname.split(".")
      dreamNumber = getDreamNumber[0] # the order number of the dream
      dreamname2 = getDreamNumber[1][1::] #the dream name only without the number
      #print (index)
      print(dreamNumber)
      print (dreamname2)
      print (date)
      print (purelink)
      print()
      response = requests.get(link) #get the dream page
      dreampage = str(response.content)
      dreamphoto = ""
      dreammp3 = ""
      dreamtext = ""
      print(dreampage)

      
