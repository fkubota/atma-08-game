# atma-08-game
[atmacup #8](https://www.guruguru.science/competitions/13/) のリポジトリ

## Basics
- コンペ期間
    - 2020/12/04 18:00 ~ 2020/12/13 18:00 (Asia/Tokyo)

- Data
    - train.shape = (8359, 16)
    - test.shape = (8360, 11)


## Feture
|カラム名|	説明	|例|
|---|---|---|
|Name|	ソフトの名前	|Aquaman: Battle for Atlantis|
|Platform|	動作するプラットフォーム名	|XB|
|Year_of_Release	|発売された年度	||
|Genre|	ゲームのジャンル	|Action|
|Publisher|	発売元	|Unknown|
|Critic_Score|	https://www.metacritic.com/ でのレビュースコアのうち、評論家によるレビュースコア	|26|
|Critic_Count|	評論家によるレビュー数|	13|
|User_Score|	ユーザーによるレビュースコア	|2.7|
|User_Count|	ユーザーによるレビューの数	|15|
|Developer|	開発会社	|Lucky Chicken|
|Rating|	ゲームの https://www.esrb.org/ によるレーティング	|T|
|NA_Sales*|	北アメリカ(NorthAmerica)での販売量	|1|
|EU_Sales*|	ヨーロッパでの販売量	|0|
|JP_Sales*|	日本での販売量	|0|
|Other_Sales*|	上記以外の国と地域での販売量	|0|
|Global_Sales*|	世界全体での販売量	|1|

*はtrainにしかない

## Log
### 20201204
- Join!!!
- nb001
    - edaした
    - targetは `Global_Salse`
    - trainにあって、testにないカラム
        - ['JP_Sales', 'Global_Sales', 'NA_Sales', 'Other_Sales', 'EU_Sales']

- nb002
    - とりあえずモデル作る
    - 使った特徴量(nanはあるけど、他は数字の特徴量)
        - ['Critic_Score', 'Critic_Count', 'User_Count']
    - result
        - cv: 1.64816
        - sub: 	1.6045

- nb003
    - eda part2
    - User_Scoreについて
        - 数値に見えるが、'30'みたいに、ストリングが入ってた。
        - 'tbd'があるが、これは `To Be Determined` の略らしい。nanに置き換えよう。
        - nan は `hoge is np.nan` がTrueになるようだ。

- nb004 
    - nb003の解析を元にnot objectの特徴量でサブ
        - `use_col = ['Year_of_Release', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']`
    
    - result
        - cv: 1.51371


- nb005
    - string特徴量を見てみた
    - 特徴量名: `feat_string = ['Platform', 'Genre', 'Publisher', 'Developer', 'Rating']`
    - nunique

    <img src='./../data/info/readme/001.png' width='400'>

    - value_counts

    <img src='./../data/info/readme/002.png' width='400'>