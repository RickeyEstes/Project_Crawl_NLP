from newspaper import Article

url = 'http://www.tapchiyhocduphong.vn/tap-chi-y-hoc-du-phong/2020/01/vac-xin-mvvac-tu-chung-vi-rut-soi-aik-c-tinh-an-toan-va-kha-nang-sinh-mien-dich--o81E2092D.html'
def write(url):
    article = Article(url, language='vi')
    article.download()
    article.parse()
    title = article.title
    text = article.text
    print(title)
    print(text)
    # with open("./DataCrawl/" + article.title.replace("/", " ").replace("?", " ").replace("-", " ").replace('"', ' ') + '.txt',
    #           'w+', encoding='utf-8') as f:
    #     f.write(article.title)
    #     f.write(article.text)
    with open("./DataCrawl/" + article.title.replace(":", " ").replace("/", " ").replace("?"," ").replace("-", " ").replace('"', ' ') + '.txt', 'w+', encoding='utf-8') as f:
        f.write(article.title)
        f.write(article.text)

write(url)
