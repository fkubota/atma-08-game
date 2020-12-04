# atma-08-game
[atmacup #8](https://www.guruguru.science/competitions/13/) のリポジトリ

## Basics
- コンペ期間
    - 2020/12/04 18:00 ~ 2020/12/13 18:00 (Asia/Tokyo)

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