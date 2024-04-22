# YouTube Data Analytics

**Introduction**

YouTube Data Analytics is a project aimed at developing a user-friendly Streamlit application that leverages the power of the Google API to extract valuable information from YouTube channels. The extracted data is then stored in a Pandas DataFrame, subsequently migrated to a SQL data warehouse, and made accessible for analysis and exploration within the Streamlit app.

**Table of Contents**

1. Key Technologies and Skills
2. Installation
3. Usage
4. Features
5. Retrieving data from the YouTube API
6. Cleaning data using Pandas
7. Migrating data to a SQL data warehouse
8. Data Analysis
9. Contributing
10. Contact

**Key Technologies and Skills**
- Python scripting
- Data Collection
- API integration
- Streamlit
- Data Management using SQL

**Installation**

To run this project, you need to install the following packages:
```python
pip install google-api-python-client
pip install pandas
pip install sqlalchemy
pip install streamlit
```

**Usage**

To use this project, follow these steps:

1. Clone the repository: ```gh repo clone AkashScoder/Youtube-Data-Analytics```
2. Install the required packages: ```pip install -r requirements.txt```
3. Run the Streamlit app: ```streamlit run my_application.py```
4. Access the app in your browser at ```http://localhost:8501```

**Features**

- Retrieve data from the YouTube API, including channel information videos, and comments.
- Store the retrieved data in a Pandas DataFrame.
- Migrate the data to a SQL data warehouse.
- Perform queries on the SQL data warehouse.
- Use streamlit to access the results and display it.
- Gain insights into channel performance, video metrics, and more.

**Retrieving data from the YouTube API**

The project utilizes the Google API to retrieve comprehensive data from YouTube channels. The data includes information on channels, playlists, videos, and comments. By interacting with the Google API, we collect the data and merge it into a list.

**Storing data in Pandas Dataframe**

The retrieved data is stored in a Pandas Dataframe. To ensure compatibility with a structured format, the data is cleansed using the powerful pandas library. .

**Migrating data to a SQL data warehouse**

The application allows users to migrate data from Pandas Dataframe to a SQL data warehouse. Users can choose which channel's data to migrate. Following data cleaning, the information is segregated into separate tables, including channels videos, and comments, utilizing SQL queries.

**Data Analysis**

The project provides comprehensive data analysis capabilities using  Streamlit.

- **Channel Analysis:** Channel analysis includes insights on playlists, videos, subscribers, views, likes, comments, and durations. Gain a deep understanding of the channel's performance and audience engagement.

- **Video Analysis:** Video analysis focuses on views, likes, comments, and durations, enabling both an overall channel and specific channel perspectives. Gain a deep understanding of the videos in a playlist

- **Comment Analysis:** Comment analysis focuses on comment ID, comment_text, comment_Published date. Gain understanding of the video impact.

The Streamlit app provides an intuitive interface to  to focus on specific aspects of the analysis.

With the  capabilities of  Streamlit, the Data Analysis section empowers users to uncover valuable insights and make data-driven decisions.

**Contributing**

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.

**Contact**

📧 Email: notifyak2002@gmail.com 

🌐 LinkedIn: ['https://www.linkedin.com/in/akash-s-717698208/')

For any further questions or inquiries, feel free to reach out. We are happy to assist you with any queries.
