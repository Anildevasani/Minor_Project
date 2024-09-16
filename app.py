import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # fetch unique users
    user_details = df['user'].unique().tolist()
    if 'Group Notification' in user_details:
        user_details.remove('Group Notification')


    user_details.sort()
    user_details.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis as", user_details)

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_msgs, words, num_med, link = helper.fetch_stats(selected_user, df)
        st.title("OverAll Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_msgs)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_med)
        with col4:
            st.header("Links Shared")
            st.title(link)

        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['msg'],color='green')
        plt.xticks(rotation=90)
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['date'], daily_timeline['msg'], color='black')
        plt.xticks(rotation=90)
        st.pyplot(fig)

        # activity map
        st.title('Activity Map')
        col1,col2 = st.columns(2)
        active_month_df, month_list, month_msg_list, active_day_df, day_list, day_msg_list =helper.activity_map(selected_user,df)
        with col1:
            st.header("Most Active Month")
            fig,ax = plt.subplots()
            ax.bar(active_month_df['month'],active_month_df['msg'])
            ax.bar(month_list[month_msg_list.index(max(month_msg_list))],max(month_msg_list),color='green',label='Highest')
            ax.bar(month_list[month_msg_list.index(min(month_msg_list))], min(month_msg_list), color='red',label='Lowest')

            plt.xticks(rotation=90)
            st.pyplot(fig)

        with col2:
            st.header("Most Active Day")
            fig, ax = plt.subplots()
            ax.bar(active_day_df['day'],active_day_df['msg'])
            ax.bar(day_list[day_msg_list.index(max(day_msg_list))], max(day_msg_list), color='green',
                   label='Highest')
            ax.bar(day_msg_list[day_msg_list.index(min(day_msg_list))], min(day_msg_list), color='red',
                   label='Lowest')
            plt.xticks(rotation=90)
            st.pyplot(fig)



        # finding the busiest users in the group(Group level)
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x,percent = helper.most_chaty(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x,color='violet')

                st.pyplot(fig)
            with col2:
                st.dataframe(percent)

        # WordCloud
        df_wc = helper.create_wordcloud(selected_user,df)
        st.title('Most Common Words')
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words


        # emoji analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df['Count'].head(), autopct="%0.2f")
            ax.set_title("Top Emojis")
            st.pyplot(fig)


