

#  BeautifulSoup 


from bs4 import BeautifulSoup 
import requests


site = "https://books.toscrape.com/"

html = requests.get(site)

html_content = html.text

soup = BeautifulSoup(html_content , "html.parser")


#===========================================================


# Common Methods in BeautifulSoup


#1.  Access first occurrence tag

print( soup.h1 ,       # whole tag
       soup.h1.text     # text inside tag
       )


#-------

#2.  find() Method

print(
          soup.find("h3")            ,# only find first and one h3 &&
          soup.find("h3").text         ,# text inside tag

          soup.find("h1", class_="description")     #Find a tag with specific attributes:
)

#-------

#3.  find_all() Method

print(     soup.find_all("a")                 ,# Finds all matching elements
           soup.find_all("a")[4]['href']      # Gets the title attribute of the 5th <a> tag , in list of a [ 0 , 1 , ..]
 
      )


#------

#4.   Using select() and select_one()

print(
        soup.select_one("p.price_color").text     ,# Select elements using CSS selectors.
        soup.select("p.price_color")[5].text         # create the list of all matching tags , and give specific 5 inx tag text
)