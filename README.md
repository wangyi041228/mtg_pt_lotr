# MTG Pro Tour The Lord of The Rings Modern Matchups
## 1 About Data
### 1.1 Data Sources
- [Pairing Round 1 (to 16) but covered by Standings](https://magic.gg/news/pro-tour-the-lord-of-the-rings-round-1-pairings)
- [Results Round 1 (to 16)](https://magic.gg/news/pro-tour-the-lord-of-the-rings-round-1-results)
- [Standings Round 1 (to 16)](https://magic.gg/news/pro-tour-the-lord-of-the-rings-round-1-standings)
- [269 Decklists](https://magic.gg/news/pro-tour-the-lord-of-the-rings-modern-decklists)
### 1.2 Data Questions
#### 1.2.1 Non-standard name in Results
I don't know the outcome of 160 games with complete accuracy. I can guess most of them. I got data based on Standings instead.

#### 1.2.2 Wrong Data in Standings
- `Mo, Jiantao` had nickname `?, ??`. He had a lot of wrong scores.
- `Xu, Yucheng` had nickname `??, ?`, `Xu, Yucheng (an extra space)` and `Yucheng Xu`. He had a lot of wrong scores.
- `Woodward, Warren` is missing since Round 1.
- `Fong, Fredrick` is missing since Round 9.
- `Vuono, Federico` is missing since Round 10.
- `Schlom, Christoph` got 2 score2 in Round 10.
- `Minniear, Matthew` lose 1 socre in Round 10.

|Round|7|8|9|10|11|12|13|14|15|16|
|---|---|---|---|---|---|---|---|---|---|---|
|Mo, Jiantao|15|12<br>15?|15|15|15<br>18?|18|15<br>18?|18|18|21|
|Xu, Yucheng|12|15<br>12?|12|12|15|15<br>18?|21|21|24|27|
|Schlom, Christoph|4|7|7|9|9|9|9|9|9|9|
|Minniear, Matthew|4|4|4|3|3|3|3|3|3|3|

- I assume they had correct scores in most rounds.
- `Mo, Jiantao` and `Xu, Yucheng` might play in wrong seats.
- I assume `Anzai, Yasunobu` vs. `Xu, Yucheng`(W), `Gunn, Thomas`(W) vs `Mo, Jiantao` in Round 12.
```
Anzai, Yasunobu	vs.	Mo, Jiantao	Yucheng Xu won 2-1-0
Gunn, Thomas	vs.	Xu, Yucheng	Thomas Gunn won 2-0-0
```
#### 1.2.3 Decklist Details
I didn't go throung every decklist, just checked the filenames.

### 1.2.4 Including and Exclusion Rules
- No Mirror Games
- No Intentional Draw (only 1,`Nielsen, Simon` vs `Beardsley, Jake` in Round 16)
- No Bye Win (including awarded bye and assigned bye)

## 2 Similar Projects
### 2.1 Krank Karsten's chart
He posted [his chart](https://twitter.com/karsten_frank/status/1685544278301282304) hours before mine. We had data a little different.
