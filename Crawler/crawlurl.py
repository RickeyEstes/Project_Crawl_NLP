import newspaper
from newspaper import Article

def newspaper_url(url):
    web_paper = newspaper.build(url, language="vi", memoize_articles=False)
    print("Extracting news pages url!!!")
    for article in web_paper.articles:
        print("News page url:", article.url)
        newspaper_information(article.url)

    print("Total acquisition%s Article" % web_paper.size())  # Number of articles

def newspaper_information(url):
    # Create links and download articles
    article = Article(url, language='vi')
    article.download()
    article.parse()
    title = article.title
    with open("./SucKhoe/" + article.title.replace(".", " ").replace("_", " ").replace(",", " ").replace(":", " ").replace("/", " ").replace("?"," ").replace("-", " ").replace('"', ' ') + '.txt', 'w+', encoding='utf-8') as f:
        f.write(article.title + ".")
        f.write(article.text)


if __name__ == "__main__":
    web_lists = ["https://doctors24h.vn/suc-khoe-doi-song.html"]
    for web_list in web_lists:
        newspaper_url(web_list)
