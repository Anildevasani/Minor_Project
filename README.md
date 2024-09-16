A Comprehensive Data Analysis on a WhatsApp Group Chat
Overview
1.Introduction
2.Data Retrieval & Preprocessing
3.Exploratory Data Analysis
4.Data Visualization
5.Data Interpretation
6.Summarizing the Inferences
7.Conclusion

Introduction:
Whatsapp has quickly become the world’s most popular text and voice messaging application. Specializing in cross-platform messaging with over 1.5 billion monthly active users, this makes it the most popular mobile messenger app worldwide.

I thought of various projects on which I could analyse data like - Air Quality Index or The cliched Covid-19 Data Analysis.

But I thought why not do Data Analysis on a WhatsApp group chat of college students and find out interesting insights about who is most active, who are ghosts (the ones who do not reply), my sleep schedule, the most used emoji, the sentiment score of each person, who swears the most, the most actives times of the day, or does the group use phones during college teaching hours?

These would be some interesting insights for sure, more for me than for you, since the people in this chat are people I know personally.

Beginning. How do I export my conversations? From Where To Obtain Data?
The first step is Data Retrieval & Preprocessing, that is to gather the data. WhatsApp allows you to export your chats through a .txt format.

Go to the respective chat, which you want to export!


Tap on options, click on More, and Export Chat.

I will be Exporting Without Media.
NOTE:
Without media: exports about **40k messages **
With media: exports about 10k messages along with pictures/videos
While exporting data, avoid including media files because if the number of media files is greater than certain figure then not all the media files are exported.

Opening this .txt file up, you get messages in a format that looks like this:


Importing Necessary Libraries
We will be using :

Regex (re) to extract and manipulate strings based on specific patterns.
References:
Regex - Python Docs
Regex cheatsheet
Regex Test - live
Datetime Format
pandas for analysis.
matlotlib and seaborn for visualization.
emoji to deal with emojis.
References:
Python Docs
Emoji
EMOJI CHEAT SHEET
wordcloud for the most used words.


Data Analysis
1. Overall frequency of total messages on the group.

2. Top 10 most active days.

3. Top 10 active users on the group (with a twist).

Ghosts present in the group. (shocking results.)
4. Top 10 users most sent media.

5. Top 10 most used emojis.

6. Most active hours and days.

Heatmaps of weekdays and months.
Most active hours, weekdays, and months.
7. Most used words - WordCloud

