from ez_aio import aio
from bs4 import BeautifulSoup


def main():
    urls = [
        f'https://magic.gg/news/pro-tour-the-lord-of-the-rings-round-{i}-results' for i in range(1, 17)
    ]
    results = aio.get(urls)
    for i, result in enumerate(results):
        with open(f'raw/results/{i + 1}.html', 'w', encoding='utf-8') as f:
            f.write(result)

    urls = [
        f'https://magic.gg/news/pro-tour-the-lord-of-the-rings-round-{i}-standings' for i in range(1, 17)
    ]
    results = aio.get(urls)
    for i, result in enumerate(results):
        with open(f'raw/standings/{i + 1}.html', 'w', encoding='utf-8') as f:
            f.write(result)

    # https://magic.gg/news/pro-tour-the-lord-of-the-rings-modern-decklists
    urls = [
        f'https://magic.gg/decklists/pro-tour-the-lord-of-the-rings-modern-decklists-{line}' for line in [
            'a-d', 'e-j', 'k-n', 'o-s', 't-z',
        ]
    ]
    results = aio.get(urls)
    for i, result in enumerate(results):
        with open(f'raw/decklists_raw/{i + 1}.html', 'w', encoding='utf-8') as f:
            f.write(result)

    urls = []
    files = [f'raw/decklists_raw/{i}.html' for i in range(1, 6)]
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'lxml')
            decks = soup.find_all('div', {'class': 'css-sBoYm css-3X0PN'})
            urls.extend([f"https://s3-us-west-1.amazonaws.com/hvn-decklist.magic.gg/"
                         f"{deck['id'].replace('%25', '%')}.json" for deck in decks])
    results = aio.get(urls)
    for i, result in enumerate(results):
        if not result:
            print(urls[i])
            continue
        fname = urls[i].rsplit('/', 1)[1].replace('%20', ' ').split('_Pro Tour The Lord of The Rings_28 July 2023_')[0] + '.json'
        with open(f"raw/decklists/{fname}", 'w', encoding='utf-8') as f:
            f.write(result)


if __name__ == '__main__':
    main()
