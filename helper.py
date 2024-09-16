from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num_msgs = df.shape[0]

    # fetch the total number of words
    words = []
    for msg in df['user']:
        words.extend(msg.split(' '))

    # fetch number of media messages
    num_med = df[df['msg'] == '<Media omitted>\n'].shape[0]

    # fetch number of links shared
    link = []
    for msg in df['msg']:
        link.extend(extract.find_urls(msg))

    return num_msgs,len(words),num_med,len(link)

def most_chaty(df):
    x = df['user'].value_counts().head()
    percent = round((df['user'].value_counts() / df.shape[0]) * 100, 2)

    return x,percent

def create_wordcloud(selected_user,df):


    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(df['msg'].str.cat(sep=''))
    return df_wc






def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month'])['msg'].count().reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby('date')['msg'].count().reset_index()

    return timeline

def activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    active_month_df=df.groupby('month')['msg'].count().reset_index()
    month_list=active_month_df['month'].tolist()
    month_msg_list=active_month_df['msg'].tolist()

    active_day_df=df.groupby('day')['msg'].count().reset_index()
    day_list=active_day_df['day'].tolist()
    day_msg_list=active_day_df['msg'].tolist()

    return active_month_df,month_list,month_msg_list,active_day_df,day_list,day_msg_list


def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for msg in df['msg']:
        emojis.extend([c for c in msg if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(),columns=['Emoji','Count'])

    return emoji_df

