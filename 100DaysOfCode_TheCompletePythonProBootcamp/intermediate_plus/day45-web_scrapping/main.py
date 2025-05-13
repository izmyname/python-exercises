from bs4 import BeautifulSoup 
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")

# get articles' titles and links
articles_text = []
articles_links=[]
articles = soup.find_all(name ="span", class_="titleline")

for article in articles:
    article_title = article.getText()
    article_title = article_title.split(" ")
    article_text = ' '.join(article_title[:-1:])
    articles_text.append(article_text)
    article_link = article.find("a")
    article_link = article_link.get("href")
    articles_links.append(article_link)

# get articles' upvotes 
articles_upvotes = []
upvotes = soup.find_all(name='span', class_='score')
for upvote in upvotes:
    upvote_text = upvote.getText()
    upvote_text = int(upvote_text.split(" ")[0])
    articles_upvotes.append(upvote_text)


# print all data
# print(articles_text)
# print(articles_links)
# print(articles_upvotes)

# get the highest article upvotes number index
max_index = articles_upvotes.index(max(articles_upvotes))
print(f"The most upvoted article:\n\nTitle: {articles_text[max_index]}\nLink: {articles_links[max_index]}\nUpvotes: {articles_upvotes[max_index]}")


# with open("./website.html", "r") as website:
#     contents = website.read()
    
# soup = BeautifulSoup(contents, "html.parser")

# all_anchors = soup.find_all(name="a")

# # for tag in all_anchors:
#     # print(tag.getText())
#     # print(tag.get("href"))
    

# company_url = soup.select_one(selector="p a")

# print(company_url)

