import pandas as pd
import datetime


import streamlit as st

st.title('各国のリーダーによるツイート')

st.sidebar.write("""
どの国のリーダーのツイートを確認しますか。
""")


reference_country = st.sidebar.selectbox(
    'どの国のリーダーのツイートを確認しますか',
    ('アメリカ','日本','イギリス',
    'ドイツ','フランス','カナダ',
    'イタリア','中国','韓国'),
)

country_list = {"アメリカ":"United States", "イギリス":"United Kingdom", "日本":"Japan","イタリア":"Italy",
            "ドイツ":"Germany","フランス":"France","カナダ":"Canada","中国":"China","韓国":"South Korea"}

df = pd.read_excel('tweet_history.xlsx')
leaders = pd.read_excel('world_politics_leaders_account.xlsx')
country = country_list[reference_country]
#leader_account = leaders['twitter_screen_names'][leaders['country'].str.contains(country)].values
leader_account = leaders[leaders['country'].str.contains(country)]


leader = st.sidebar.selectbox(
    'リーダー',
    (leader_account['twitter_names']))

leader_screen_name = leader_account['twitter_screen_names'][leaders['twitter_names'] == leader].values[0]

display_start = st.button('start')

if display_start:
    
    result = df[df['screen_name'] == leader_screen_name].sort_values('date', ascending=False)
    for tweet_text,tweet_date in zip(result['tweet_ja'].values,result['date'].values):
        tweet_date = pd.to_datetime(tweet_date)
        tweet_date
        st.markdown(tweet_text)
        ''
        ''
        #st.text(tweet_text)


    #st.dataframe(result['tweet_ja'])



