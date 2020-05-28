import newspaper
from newspaper import Article

def spider_newspaper_url(url):
    web_paper = newspaper.build(url, language="vi", memoize_articles=False)
    print("Extracting news pages url!!!")
    for article in web_paper.articles:
        print("News page url:", article.url)
        spider_newspaper_information(article.url)

    print("Total acquisition%s Article" % web_paper.size())  # Number of articles

def spider_newspaper_information(url):
    # Create links and download articles
    article = Article(url, language='vi')
    article.download()
    article.parse()
    title = article.title
    # title.replace("/", "-")
    with open("./yte/" + article.title.replace("/", " ").replace("?"," ").replace("-", " ").replace('"', ' ') + '.txt', 'w+', encoding='utf-8') as f:
        f.write(article.text)
    # print("html=", article.html)
# Getting information about articles
#     print("<title>", article.title, "</title>")  # Get the title of the article
#     print("<text>", article.text, "</text>\n")  # Get the text of the article


if __name__ == "__main__":
    web_lists = ["https://www.thuocbietduoc.com.vn/thuoc-66103/levobupibfs-75mg.aspx"]
    for web_list in web_lists:
        spider_newspaper_url(web_list)
