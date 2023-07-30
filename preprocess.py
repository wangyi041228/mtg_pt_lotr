from bs4 import BeautifulSoup
import os
import json
import pandas

names_lib = {
    # 'AntonioGuzVaz93': 'JOSE ANTONIO GUZMAN VAZQUEZ',
    # 'Teyi': 'Jean Zarrouati',
    # 'GliedTamas': 'Tamás Glied',
    # 'Garthmorr': 'Bassel Nasri',
    # 'NicolasB': 'Nicolas BORGEL Larchevêque',
    # 'martos': 'Toni Martos',
    # '__DELBAS': 'FEDERICO DEL BASSO',
    # 'kazuyaterasawa': 'kazuya terasawa',
    # 'Malekz': 'Joaquin facundo Maletti',
    # 'matheusponciano': 'Matheus Ponciano',
    # 'Jpsn54': '',
    # 'Kafit5566': '',
    # 'Ibirrell': '',
    # 'Lostwanderer': '',
    # 'Masonme2': '',
}
names_lib2 = {
    '?, ??': 'Mo, Jiantao',
    '??, ?': 'Xu, Yucheng',
    'Xu, Yucheng ': 'Xu, Yucheng',
    'Yucheng Xu': 'Xu, Yucheng',
}
names_lib3 = {
    'MORIYAMA, MASAHIDE': 'Masahide Moriyama',
    'Santos, André': 'Andr%C3%A9 Santos',
    'KONDO, SHOGO': 'Shogo Kondo',
    'CHANG, CHENG YU': 'Cheng Yu Chang',
    'BORGEL Larchevêque, Nicolas': 'Nicolas Borgel',
    'asaumi, hiroki': 'Hiroki Asaumi',
    'Rohrböck, Michael': 'Michael Rohrb%C3%B6ck',
    'GUZMAN VAZQUEZ, JOSE ANTONIO': 'Antonio Guzman',
    'terasawa, kazuya': 'Kazuya Terasawa',
    'Tóth, Jakub': 'Jakub T%C3%B3th',
    'HENG, CHYE HWEE': 'Chye Hwee Heng',
    'Sánchez Peralta, Archibal Raziel': 'Archibal Raziel S%C3%A1nchez Peralta',
    'Maletti, Joaquin facundo': 'Joaquin Facundo Maletti',
    'Jirkal, Tomáš': 'Tom%C3%A1%C5%A1 Jirkal',
    'ruel-mailfert, olivier': 'Olivier Ruel-Mailfert',
    'Almeida, Álvaro': '%C3%81lvaro de Almeida',
    'nakamura, shuhei': 'Shuhei Nakamura',
    'DEL BASSO, FEDERICO': 'Federico Del Basso',
    'hongchen, jiao': 'Hongchen Jiao',
    'FENG, YANG': 'Yang Feng',
    'wu, tianyou': 'Tianyou Wu',
    'Dong, Sui': 'Dong Sui',
    'Glied, Tamás': 'Tam%C3%A1s Glied',
    'qiang, lei': 'Lei Qiang',
    'Solano, Jesús': 'Jes%C3%BAs Solano',
    'cammilluzzi, Marco': 'Marco Cammilluzzi',
    'watanabe, takanori': 'Takanori Watanabe',
    'Schütz, Stefan': 'Stefan Sch%C3%BCtz',
    'Pardee, Samuel': 'Sam Pardee',
    'goutbeek, jitse': 'Jitse Goutbeek',
    'Neves, José': 'Jos%C3%A9 Neves',
    'mechin, thomas': 'Thomas Mechin',
    'Casatti, Vagner William': 'Vagner Casatti',
    'YU, HUNGYI': 'HungYi Yu',
    'escalante, josue': 'Josue Escalante',
    'Lee, Shang Feng': 'Anthony Lee',
    'Elçi, Berk': 'Berk El%C3%A7i',
    'sun, chuan': 'Chuan Sun',
    'LAGARDE, Antoine': 'Antoine Lagarde',
    'Jacques-Griffin, Théo': 'Th%C3%A9o Jacques-Griffin',
    'Carvalho, Marcio': 'M%C3%A1rcio Carvalho',
    'Yung-Ming, Huang': 'Yung-Ming Huang',
    'Vu, Quang (Duy)': 'Duy Vu',
    'hara, kouki': 'Kouki Hara',
    'YUYA, TASE': 'Yuya Tase',
    'miranda, claudio': 'Claudio Miranda',
    'Simões, Miguel': 'Miguel Sim%C3%B5es',
    'Calzada Tovar, Jesús Adán': 'Ad%C3%A1n Calzada',
    'Judd, Andre': 'Andr%C3%A9 Judd',
    'martinez, gabriel': 'Gabriel Martinez',
    'nakayama, satoshi': 'Satoshi Nakayama',
    'Bin, Jia': 'Bin Jia',
    'Rieu-Helft, Raphaël': 'Rapha%C3%ABl Rieu-Helft',
    'Gutiérrez von Porat, Nils': 'Nils Guti%C3%A9rrez von Porat',
    'Minniear, Matthew ': 'Matthew Minniear',
    'TAN, RICHMOND': 'Richmond Tan',
    'pontes, Israel': 'Israel Pontes',
}


def std_name(name):
    if ',' in name:
        name = ' '.join(name.split(', ')[::-1])
    return name


# Abandon
def main():
    for i in range(1, 17):
        print(f'ROUND {i}')
        with open(f'raw/results/{i}.html', 'r', encoding='utf-8') as f:
            result = f.read()
            soup = BeautifulSoup(result, 'lxml')
            tbody = soup.find('tbody')
            trs = tbody.find_all('tr')
            for tr in trs:
                tds = tr.find_all('td')
                p1 = std_name(tds[0].text)
                p2 = std_name(tds[2].text)
                info = tds[3].text
                if info.endswith(' bye'):
                    ...
                    print('BYE', p1, info, sep=' | ')
                elif info.endswith(' Draw'):
                    ...
                    # print('DRAW', p1, p2, sep=' | ')
                elif 'won' in info:
                    winner, score = info.split(' won ', 1)
                    if winner in names_lib:
                        winner = names_lib[winner]
                    ...
                    if p1 == winner or p2 == winner:
                        ...
                    else:
                        print('WON', p1, p2, info, p1 == winner or p2 == winner, sep=' | ')
                else:
                    print('WRONG')
                    print(p1, p2, info, sep=' | ')


def player_infos():
    infos = {}
    for i in range(1, 17):
        print(f'ROUND {i}')
        with open(f'raw/standings/{i}.html', 'r', encoding='utf-8') as f:
            result = f.read()
            soup = BeautifulSoup(result, 'lxml')
            tbody = soup.find('tbody')
            trs = tbody.find_all('tr')
            for tr in trs:
                tds = tr.find_all('td')
                if not tds:
                    continue
                t0 = int(tds[0].text)
                t1 = tds[1].text
                if t1 in names_lib2:
                    t1 = names_lib2[t1]
                t2 = int(tds[2].text)
                t3 = float(tds[3].text)
                if t1 not in infos:
                    infos[t1] = [0, []]
                delta = t2-infos[t1][0]
                if delta not in [0, 1, 3]:
                    print(t1, delta)
                infos[t1][1].append([delta, t0, t3])
                infos[t1][0] = t2

    files = os.listdir('raw/decklists')
    deckinfos = {}
    deckcount = {}
    for file in files:
        deck, player = file[:-5].rsplit('_', 1)
        deck = deck.replace('_', ' ')
        deckinfos[player] = deck
        if deck in deckcount:
            deckcount[deck] += 1
        else:
            deckcount[deck] = 1
    with open('deck_type_count.txt', 'w', encoding='utf-8') as f:
        print(json.dumps(deckcount, ensure_ascii=False, indent=2), file=f)
    with open('deck_infos.txt', 'w', encoding='utf-8') as f:
        print(json.dumps(deckinfos, ensure_ascii=False, indent=2), file=f)
    for player in infos:
        if player in names_lib3:
            _nickname = names_lib3[player]
        else:
            _nickname = std_name(player)
        if _nickname in deckinfos:
            infos[player].append(deckinfos[_nickname])
        else:
            print(player)

    with open('standings_info.txt', 'w', encoding='utf-8') as f:
        print(json.dumps(infos, indent=2, ensure_ascii=False), file=f)
    infos['Fong, Fredrick'][1].append(infos['Fong, Fredrick'][1][-1])
    infos['Vuono, Federico'][1].append(infos['Fong, Fredrick'][1][-1])
    infos['Woodward, Warren'] = [0, [[0, 0, 0.0]], 'Mardu Burn']
    infos['Mo, Jiantao'][1][7][0] = 0
    infos['Mo, Jiantao'][1][8][0] = 0
    infos['Mo, Jiantao'][1][10][0] = 3
    infos['Mo, Jiantao'][1][11][0] = 0
    infos['Mo, Jiantao'][1][12][0] = 0
    infos['Xu, Yucheng'][1][7][0] = 0
    infos['Xu, Yucheng'][1][8][0] = 0
    infos['Xu, Yucheng'][1][10][0] = 0
    infos['Xu, Yucheng'][1][11][0] = 3
    infos['Xu, Yucheng'][1][12][0] = 3
    with open('standings_info_fixed.txt', 'w', encoding='utf-8') as f:
        print(json.dumps(infos, indent=2, ensure_ascii=False), file=f)


def main2():
    with open('standings_info_fixed.txt', 'r', encoding='utf-8') as f:
        infos = json.loads(f.read())
    with open('deck_type_count.txt', 'r', encoding='utf-8') as f:
        deckcount = json.loads(f.read())
        deckcount2 = sorted(deckcount.items(), key=lambda a: a[1], reverse=True)
        decktypes = [x[0] for x in deckcount2]
        print(*decktypes, sep='\n')
        size = len(decktypes)
        dict_deck2index = {decktypes[i]: i for i in range(size)}
        dict_index2deck = {i: decktypes[i] for i in range(size)}
        matchups = [[[0, 0, 0] for x in range(size + 1)] for y in range(size + 1)]  # [win, draw, lose]
    for i in [3, 4, 5, 6, 7, 11, 12, 13, 14, 15]:
        print(f'ROUND {i+1}')
        with open(f'raw/results/{i+1}.html', 'r', encoding='utf-8') as f:
            result = f.read()
            soup = BeautifulSoup(result, 'lxml')
            tbody = soup.find('tbody')
            trs = tbody.find_all('tr')
            for tr in trs:
                tds = tr.find_all('td')
                p1 = tds[0].text
                if p1 in names_lib2:
                    p1 = names_lib2[p1]
                p2 = tds[2].text
                if p2 in names_lib2:
                    p2 = names_lib2[p2]
                if p1 not in infos or (p2 not in infos and p2 != '-'):
                    print('MISSING', tr)
                    continue

                if p2 == '-':
                    continue

                info = tds[3].text
                if i == 11:
                    if p1 == 'Anzai, Yasunobu':
                        p2 = 'Xu, Yucheng'
                    elif p1 == 'Gunn, Thomas':
                        p2 = 'Mo, Jiantao'

                if i > len(infos[p1][1]) - 1:
                    score1 = 0
                    print(i+1, p1)
                else:
                    score1 = infos[p1][1][i][0]
                    deck1 = infos[p1][2]
                    index1 = dict_deck2index[deck1]
                if i > len(infos[p2][1]) - 1:
                    score2 = 0
                    print(i+1, p2)
                else:
                    score2 = infos[p2][1][i][0]
                    deck2 = infos[p2][2]
                    index2 = dict_deck2index[deck2]

                if info.endswith(' bye'):
                    ...
                    # print('BYE', p1, info, sep=' | ')
                elif info.endswith(' Draw'):
                    if (score1, score2) == (1, 1):
                        if deck1 == deck2:
                            continue
                        if info.startswith('0-0-3'):
                            print('ID', p1, p2, info, sep=' | ')
                            continue
                        matchups[index1][index2][1] += 1
                        matchups[index2][index1][1] += 1
                    else:
                        print('WRONG', p1, p2, info, infos[p1][1][i], infos[p2][1][i], sep=' | ')
                    # print('DRAW', p1, p2, sep=' | ')
                elif 'won' in info:
                    winner, score = info.split(' won ', 1)
                    if (score1, score2) in ((3, 0), (0, 3)):
                        if deck1 == deck2:
                            continue
                        if score1 == 3:
                            matchups[index1][index2][0] += 1
                            matchups[index2][index1][2] += 1
                        if score1 == 0:
                            matchups[index1][index2][2] += 1
                            matchups[index2][index1][0] += 1
                    else:
                        print('WRONG', p1, p2, info, infos[p1][1][i], infos[p2][1][i], sep=' | ')
                else:
                    print('WRONG')
                    print(p1, p2, info, sep=' | ')

    for i in range(size):
        matchups[i][-1] = [sum(matchups[i][j][0] for j in range(size)),
                           sum(matchups[i][j][1] for j in range(size)),
                           sum(matchups[i][j][2] for j in range(size))]
    for i in range(size):
        matchups[-1][i] = [sum(matchups[j][i][0] for j in range(size)),
                           sum(matchups[j][i][1] for j in range(size)),
                           sum(matchups[j][i][2] for j in range(size))]

    with open('matchups.txt', 'w', encoding='utf-8') as f:
        print(json.dumps(matchups, ensure_ascii=False, indent=2), file=f)
    sheet = [['' for x in range(size + 1)] for y in range(size + 1)]
    for i in range(size+1):
        for j in range(size + 1):
            data = matchups[i][j]
            data_sum = sum(data)
            rate = f'{(data[0] + data[1] * 0.5) * 100 / data_sum:.1f}%' if data_sum > 0 else ''
            sheet[i][j] = f'{data[0]}-{data[1]}-{data[2]}\n{rate}' if data_sum > 0 else ''
    with open('sheet.txt', 'w', encoding='utf-8') as f:
        print(json.dumps(sheet, ensure_ascii=False, indent=2), file=f)
    x = pandas.DataFrame(sheet)
    x.to_excel('sheet.xlsx')


if __name__ == '__main__':
    player_infos()
    main2()
