# Streamlit dashboard code

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
import re

st.title('Dash Board')

st.write("""Sample Data for DAS Project""")

debate = {'#JusticeforPriyantha': """
The tweets related to "#JusticeforPriyantha" predominantly express deep sorrow and a sense of
betrayal, focusing on a call for justice in response to a specific, impactful incident.
The repeated use of the hashtag underscores a collective demand for accountability and action.
These sentiments reflect both personal anguish and a broader community reaction to what appears
to be a significant and emotionally charged event.
""",

"#pariyanthakumara": """
The tweets about "#priyanthaKumara" convey deep sorrow and remorse over a tragic incident,
with a strong emphasis on the need for accountability and legal reform. They are centered around a
specific event in Sialkot, which has profoundly affected both individual emotions and broader social
and political discourse. The conversation reflects a community in mourning, critically evaluating
societal norms and seeking meaningful change.
""",

"#sialkotincident": """
The tweets about the "#sialkotincident" are mostly in Urdu and primarily focus on a serious event
in Sialkot, Pakistan, often involving discussions around Blasphemy Law. They reflect
a high level of public concern and debate, characterized by strong and urgent reactions. The
discourse suggests significant societal, legal, and religious implications arising from this
controversial incident.
""",

"#Sialkottragedy": """
The tweets concerning the "#Sialkottragedy" predominantly express deep grief and ethical concerns,
reflecting the Pakistani community's intense reaction to a grave incident. Discussions hint at
political and governmental implications, indicating the complexity of the situation. Overall, the
discourse is marked by a mix of sorrow, moral questioning, and a search for accountability in the
wake of a distressing event.
""",

"سیالکوٹ_سانحہ#": """
The tweets about "سیالکوٹ سانحہ" (Sialkot Tragedy) predominantly focus on the Pakistani community's
reaction to a significant event in Sialkot, marked by distress and outrage. The discourse
intertwines societal concerns with religious elements, notably around blasphemy, highlighting the
complexity of the situation. Overall, the tweets reflect a deep emotional impact and a call for
societal reflection and action.
""",

"شدت_پسندی_اسلام_نہیں#": """
The tweets under "شدت پسندی اسلام نہیں" (Extremism is not Islam) reflect a strong rejection of
extremism as unrepresentative of Islam, in response to specific events demanding justice. They call
for action from military entities such as ISPR, emphasizing a societal desire for peace and unity
against extremist acts. The discourse highlights a collective stand against linking extremism with
Islamic beliefs.
"""}



def convert_df(df):
  return df.to_csv(index=False).encode('utf-8')

df = pd.DataFrame()

source = st.selectbox(
'Select your preferred data source',
('--', 'Twitter', 'Tiktok', 'Youtube', 'Facebook', 'Blogs / Editorials'))

if source == 'Twitter':
  x = st.info("👈 Select **hashtag** from the sidebar to see insights!")

genre = st.sidebar.selectbox(
"Select one hashtag",
["--", "#JusticeforPriyantha", "#pariyanthakumara", "#sialkotincident",
"#Sialkottragedy", "سیالکوٹ_سانحہ#", "شدت_پسندی_اسلام_نہیں#"])

if genre == '#JusticeforPriyantha':
    x.empty()
    df = pd.read_excel('Labelled/#Justiceforpariyantha.xlsx')
    st.markdown("## Twitter Analysis for #JusticeforPriyantha")
    sentiment_counts = df['sentiment'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    st.pyplot(plt)

    st.caption('Key Element of Debate')
    st.error(debate['#JusticeforPriyantha'])

    csv = convert_df(df)
    st.caption('Download Data')
    st.download_button(
    "Press to Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

elif genre == '#pariyanthakumara':
    x.empty()
    df = pd.read_excel('Labelled/#pariyanthakumara.xlsx')
    st.markdown("## Twitter Analysis for #pariyanthakumara")
    sentiment_counts = df['sentiment'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    st.pyplot(plt)

    st.caption('Key Element of Debate')
    st.error(debate['#pariyanthakumara'])

    csv = convert_df(df)
    st.caption('Download Data')
    st.download_button(
    "Press to Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

elif genre == '#sialkotincident':
    x.empty()
    df = pd.read_excel('Labelled/#sialkotincident.xlsx')
    st.markdown("## Twitter Analysis for #sialkotincident")
    sentiment_counts = df['sentiment'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    st.pyplot(plt)

    st.caption('Key Element of Debate')
    st.error(debate['#sialkotincident'])

    csv = convert_df(df)
    st.caption('Download Data')
    st.download_button(
    "Press to Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

elif genre == '#Sialkottragedy':
    x.empty()
    df = pd.read_excel('Labelled/#Sialkottragedy.xlsx')
    st.markdown("## Twitter Analysis for #Sialkottragedy")
    sentiment_counts = df['sentiment'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    st.pyplot(plt)

    st.caption('Key Element of Debate')
    st.error(debate['#Sialkottragedy'])

    csv = convert_df(df)
    st.caption('Download Data')
    st.download_button(
    "Press to Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

elif genre == 'سیالکوٹ_سانحہ#':
    x.empty()
    df = pd.read_excel('Labelled/سیالکوٹ_سانحہ#.xlsx')
    st.markdown("## Twitter Analysis for سیالکوٹ_سانحہ#")
    sentiment_counts = df['sentiment'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    st.pyplot(plt)

    st.caption('Key Element of Debate')
    st.error(debate['سیالکوٹ_سانحہ#'])

    csv = convert_df(df)
    st.caption('Download Data')
    st.download_button(
    "Press to Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )

elif genre == 'شدت_پسندی_اسلام_نہیں#':
    x.empty()
    df = pd.read_excel('Labelled/شدت_پسندی_اسلام_نہیں#.xlsx')
    st.markdown("## Twitter Analysis for شدت_پسندی_اسلام_نہیں#")
    sentiment_counts = df['sentiment'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    st.pyplot(plt)

    st.caption('Key Element of Debate')
    st.error(debate['شدت_پسندی_اسلام_نہیں#'])

    csv = convert_df(df)
    st.caption('Download Data')
    st.download_button(
    "Press to Download",
    csv,
    "file.csv",
    "text/csv",
    key='download-csv'
    )
