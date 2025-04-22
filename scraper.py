import requests
from bs4 import BeautifulSoup

def fetch_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

if __name__ == "__main__":
    import sys
    
    def batch_fetch_titles(urls, output_file="titles.txt"):
        results = []
        for url in urls:
            try:
                title = fetch_title(url)
                results.append(f"{url} -> {title}")
                print(f"{url} -> {title}")
            except Exception as e:
                results.append(f"{url} -> Error: {e}")
                print(f"{url} -> Error: {e}")
        with open(output_file, "w", encoding="utf-8") as f:
            for line in results:
                f.write(line + "\n")
        print(f"\nAll results saved to {output_file}")

    # 用法：python scraper.py url1 url2 ...
    if len(sys.argv) == 1:
        # 无参数，使用默认测试
        test_url = "https://www.example.com"
        print(f"Title: {fetch_title(test_url)}")
    elif len(sys.argv) == 2:
        # 单个网址
        url = sys.argv[1]
        print(f"Title: {fetch_title(url)}")
    else:
        # 多个网址
        urls = sys.argv[1:]
        batch_fetch_titles(urls)
