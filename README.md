# YouTube Data Harvesting and Warehousing 

**Introduction**

YouTube Data Harvesting and Warehousing is a project aimed at developing a user-friendly Streamlit application that leverages the power of the Google API to extract valuable information from YouTube channels. The extracted data is then stored in a MongoDB database, subsequently migrated to a SQL data warehouse, and made accessible for analysis and exploration within the Streamlit app.

**Table of Contents**

1. Key Technologies and Skills
2. Installation
3. Usage
4. Features
5. Retrieving data from the YouTube API
6. Storing data in MongoDB
7. Migrating data to a SQL data warehouse
8. Data Analysis
9. Contributing
10. License
11. Contact

**Key Technologies and Skills**
- Python scripting
- Data Collection
- API integration
- Streamlit
- Plotly
- Data Management using MongoDB (Atlas) and SQL

**Installation**

To run this project, you need to install the following packages:
```python
pip install google-api-python-client
pip install pymongo
pip install pandas
pip install psycopg2
pip install streamlit
pip install plotly
```

**Usage**

To use this project, follow these steps:

1. Clone the repository: ```git clone https://github.com/gopiashokan/Youtube-Harvesting-and-Warehousing.git```
2. Install the required packages: ```pip install -r requirements.txt```
3. Run the Streamlit app: ```streamlit run app.py```
4. Access the app in your browser at ```http://localhost:8501```

**Features**

- Retrieve data from the YouTube API, including channel information, playlists, videos, and comments.
- Store the retrieved data in a MongoDB database.
- Migrate the data to a SQL data warehouse.
- Analyze and visualize data using Streamlit and Plotly.
- Perform queries on the SQL data warehouse.
- Gain insights into channel performance, video metrics, and more.
