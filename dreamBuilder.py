import requests
import os
import sqlite3
import mysql.connector
import sys
def addDreamMYSQL(number, title, verses):
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


def addDream(date, title, words, mp3, jpg, pdf):
        conn = sqlite3.connect('dreams.db')
        conn.execute("INSERT INTO DREAMS (DATE, TITLE, WORDS, MP3, JPG, PDF) VALUES(?, ?, ?)", (date, title, words, mp3, jpg,pdf));
        conn.commit()
        print (str(number) + " " + str(title) + "  added successfully");
        conn.close()    

def insertDream(jpg, key):
        conn = sqlite3.connect('dreams.db')
        conn.execute("INSERT INTO DREAMS (JPG, KEY) VALUES(?, ?)", (jpg,key,));
        conn.commit()
        print (str(jpg) + "  added successfully");
        conn.close()    

def insertDreamPDF(pdf, key):
        conn = sqlite3.connect('dreams.db')
        conn.execute("INSERT INTO DREAMS (PDF, KEY) VALUES(?, ?)", (pdf,key,));
        conn.commit()
        print (str(pdf) + "  added successfully");
        conn.close()   
def updateDreamJPG(jpg, keyword):
        conn = sqlite3.connect('dreams.db')
        conn.execute("UPDATE DREAMS SET JPG=? WHERE KEY=?", (jpg,keyword,));
        conn.commit()
        #print (str(jpg) + "  added successfully");
        conn.close()    

def updateDreamPDF(pdf, keyword):
        conn = sqlite3.connect('dreams.db')
        conn.execute("UPDATE DREAMS SET PDF=? WHERE KEY=?", (pdf,keyword,));
        conn.commit()
        print (str(pdf) + "  added successfully");
        conn.close()  

path = "/home/giovanni/Downloads/dreams/dreams/"
print(path)
dirs = os.listdir( path )
dirs.sort()
jpgfiles = []
mp3files = []
pdffiles = []
for file in dirs:
   if ".jpg" in file:
      jpgfiles.append(file)

for file in dirs:
   if ".mp3" in file:
      mp3files.append(file)

for file in dirs:
   if ".pdf" in file:
      pdffiles.append(file)

for file in jpgfiles:
   if ".jpg" in file:
     if "." in file:
       split = file.split(".")
       key = split[0]
       updateDreamJPG(file,key)
       print(key)
     if "-" in file:
        split = file.split("-")
        key = split[0]
        updateDreamJPG(file,key)
        print(key)
"""
for file in pdffiles:
   if ".pdf" in file:
     split = file.split("_")
     key = split[1]
     #print(key)
     #print(file)
     #updateDreamPDF(file,key)
     insertDreamPDF(file,key)
#print(mp3files)
#print(pdffiles)
"""
"""
response = requests.get('http://www.formypeople.org/dreams/')
dreamtitles = str(response.content) #get the raw website content
dreamtitles = dreamtitles.split('class="date">') #extract the date and title
del dreamtitles[155:]
del dreamtitles[3:81]
dreamtitles[::-1] #delete content at the end
 # delete content at the beginning
dreamList = []
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
      #print(dreamNumber)
      #print (dreamname2)
      #print (date)
      #print (purelink)
      dreamset = [dreamNumber,dreamname2,date,purelink]
      dreamList.append(dreamset)
      #print()
      #response = requests.get(link) #get the dream page
      #dreampage = str(response.content)
      #dreamphoto = ""
      #dreammp3 = ""
      #dreamtext = ""
      #print(dreampage)



response = requests.get(dreamList[0][3])
thedream = str(response.content) #get the raw website content
count = 1
for link in dreamList:
   response = requests.get(link[3])
   thedream = str(response.content) #get the raw website content
   f = open(str(count)+"txt", "w+")
   f.write(thedream)
   f.close()
   count = count +1

# Open a file
path = "/home/giovanni/Downloads/dreams/dreams/dreams/"
print(path)
dirs = os.listdir( path )
print(dirs)
del dirs[:57]
del dirs[59:]
for file in dirs:
   f = open(path+file, "r")
   lines = f.read()
   #print(lines)


   splitthedream = lines.split("</a></audio></p>")
   photoextractor = lines.split("http") 
   jpg = ""
   pdffile = []
   mp3file = []
   for x in photoextractor:
      if "jpg" in x and "feature" in x:
          jpg = "http" + x[:x.index("jpg")+3]
      if "pdf" in x:
          pdffile.append(x)
      if "mp3" in x:
          mp3file.append(x)
   mp3filelink = "http" + mp3file[0][:mp3file[0].index('mp3')+3]   
   splitmp3= mp3filelink.split("/")
   mp3filename = ""
   for x in splitmp3:
      if "mp3" in x:
        mp3filename=x 
   print(mp3filename)
   if "mp3" in mp3filename:
     mp3_data = requests.get(mp3filelink).content
     with open(mp3filename, 'wb') as handler:
        handler.write(mp3_data)


scriptindex1 = thedream.index("<script>")
scriptindex2 = thedream.index("</script>")
print(scriptindex1)
print(scriptindex2)
splitthedream = thedream.split("<p>")
for p in splitthedream:
    if "script" in p:
       p = str(p)
       x = p.index("<script")
       y = p.index("</script>")
       del p[x:y]
       print(p)
    else:
      print (p)
    print()

"""
	
