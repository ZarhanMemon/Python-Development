import requests



site = "https://books.toscrape.com/"


# Fetch the homepage HTML
url = requests.get(site)

print( 
    url.text ,          # raw html code
    url.status_code     # 200-Ok , 500-fail , 404-not_found
    )

# Save the first page HTML
with open('htmls/_1page.html', 'w', encoding='utf-8') as f:
    f.write(url.text)

# Fetch and save all catalogue pages (1–50)
for i in range(1, 51):
    w_url = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    with open(f"htmls/Books_site/page_{i}.html", "w", encoding='utf-8') as f:
        f.write(w_url.text)
        print(f"{i} page done")



#=================================================


