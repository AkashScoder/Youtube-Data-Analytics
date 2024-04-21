import pandas as pd
from sqlalchemy import create_engine, text
import streamlit as st

# Create an SQLAlchemy engine
engine = create_engine('mysql+pymysql://root:2261389@localhost:3306/Guvi')

questions = {
    'Names of all videos and their corresponding channels': 'select video_name as Video_Name,channel.channel_name as Channel_Name from videos inner join channel on videos.playlist_id=channel.playlist_id order by channel.channel_name;',
    'Which channels have the most number of videos, and how many videos do they have?': 'select channel.channel_name as Channel_Name,count(video_id) as Total_Video_Count from videos inner join channel on videos.playlist_id=channel.playlist_id group by channel_name order by Total_video_count desc limit 5;',
    'What are the top 10 most viewed videos and their respective channels': 'select channel_name as Channel_Name,videos.video_name as Video_Name ,videos.view_count as Video_View_Count from channel inner join videos on channel.playlist_id=videos.playlist_id order by videos.view_count desc limit 10;',
    'How many comments were made on each video, and what are their corresponding video names':'select videos.video_name as Video_Name,count(comments.comment_id) as Comment_Count from videos join comments on videos.video_id=comments.video_id group by videos.video_id order by count(comments.comment_id) desc;',
    'Which videos have the highest number of likes, and what are their corresponding channel names': 'select channel.channel_name as Channel_Name, video_name as Video_Name, like_count as Video_Like_Count from videos inner join channel on videos.playlist_id=channel.playlist_id order by like_count desc limit 10;',
    'What is the total number of likes and dislikes for each video, and what are their corresponding video names': 'select video_name as Video_Name, like_count as Video_Like_Count from videos order by like_count desc;',
    'What is the total number of views for each channel, and what are their corresponding channel names': 'select channel_name as Channel_Name,channel_views as Total_Channel_Views from channel;',
    'What are the names of all the channels that have published videos in the year 2022?': 'select channel_name as Channel_Name, videos.published_year as Year_of_Publishing_2022 from channel inner join videos on channel.playlist_id=videos.playlist_id where videos.published_year=2022;',
    'What is the average duration of all videos in each channel, and what are their corresponding channel names': 'select channel_name as Channel_Name, avg(videos.duration) as Avg_Duration from channel inner join videos on channel.playlist_id=videos.playlist_id group by channel_name;',
    'Which videos have the highest number of comments, and what are their corresponding channel names': 'select channel.channel_name as Channel_Name,videos.video_name as Video_Name,videos.comment_count as Comment_Count from videos inner join channel on videos.playlist_id=channel.playlist_id group by videos.video_id,videos.video_name,channel.channel_name order by comment_count desc limit 10;'}

# Function to execute SQL queries and return results as DataFrames
def execute_query(query):
    connection = engine.connect()
    result = connection.execute(text(query))
    final_df = pd.DataFrame(result, columns=result.keys(), index=None)
    connection.close()
    return final_df


# Display query results as tables in Streamlit
st.set_page_config(
    page_title="YouTube Analytics",
    page_icon=":clapper:",
    layout="wide"
)

st.title('\t\t\tYouTube Analytics')

st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition-duration: 0.4s;
        margin-right: 10px;
    }

    .stButton button:hover {
        background-color: #45a049;
    }

    .stDataFrame div[data-baseweb="table"] {
        max-width: 100%;
        overflow-x: auto;
    }

    .stDataFrame div[data-baseweb="table"] th {
        background-color: #f2f2f2;
        font-weight: bold;
        border: 1px solid #ddd;
        padding: 12px;
        text-align: left;
    }

    .stDataFrame div[data-baseweb="table"] td {
        border: 1px solid #ddd;
        padding: 12px;
    }

    .stDataFrame div[data-baseweb="table"] tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    .stDataFrame div[data-baseweb="table"] tr:hover {
        background-color: #e6f7ff;
    }

    .stTextInput>div>div>div {
        background-color: #f2f2f2 !important;
        border-radius: 5px !important;
        border: none !important;
        padding: 10px;
    }

    .stTextInput>div>div>div>input {
        background-color: transparent !important;
        border: none !important;
        padding: 10px;
        font-size: 16px;
    }

    .stTitle {
        font-size: 32px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 20px;
        text-align: center; /* Center-align title */
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Add execute SQL button
channel_id = st.text_input("Enter Channel ID:")
if st.button("Results"):
    if channel_id:
        query = f"select channel_name as Channel_Name,subscription_count as Subscriber_Count,videos.playlist_id as Playlist_ID,videos.video_name as Video_Name,videos.publishedat as Published_Date,videos.view_count as View_Count,videos.like_count as Like_Count,videos.comment_count as Comment_count from channel inner join videos on channel.playlist_id=videos.playlist_id where channel_id='{channel_id}'"
        df = execute_query(query)
        df = df.reset_index(drop=True)
        st.markdown(f"<h2>Channel Results for Channel ID: {channel_id}</h2>", unsafe_allow_html=True)
        st.dataframe(df, height=300)

# Add execute SQL button
# sql_query = st.text_input("Enter your SQL statement:")
# if st.button("Execute SQL Statement"):
#     if sql_query:
#         df = execute_query(sql_query)
#         df = df.reset_index(drop=True)
#         st.markdown("<h2>Query Result</h2>", unsafe_allow_html=True)
#         st.dataframe(df, height=300)
#
for question, query in questions.items():
    if st.button(question):
        df = execute_query(query)
        df = df.reset_index(drop=True)
        st.markdown(f"<h2>{question}</h2>", unsafe_allow_html=True)
        st.dataframe(df, height=300)
