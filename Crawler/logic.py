from newspaper import Article

url = 'https://www.thuocbietduoc.com.vn/thuoc-66103/levobupibfs-75mg.aspx'
def write(url):
    article = Article(url, language='vi')
    article.download()
    article.parse()
    title = article.title
    text = article.text
    print(title)
    print(text)
    with open("./yte/" + article.title.replace("/", " ").replace("?", " ").replace("-", " ").replace('"', ' ') + '.txt',
              'w+', encoding='utf-8') as f:
        f.write(article.text)

write(url)
