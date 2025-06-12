**FINANCIAL INSIGHTS CHATBOT SYSTEM**

**Aim of the Project**

The aim of this project is to develop an interactive financial chatbot that provides users with real-time financial metrics—such as revenue, net income, and assets—of top companies through natural language queries. The system uses basic Natural Language Processing (NLP) to understand queries and displays corresponding financial data and dynamic charts using a web-based interface.

**Tools Used**

- **Python** – Core development and logic

- **Streamlit** – For building an interactive and responsive web interface

- **Pandas** – For data handling and analysis

- **Altair** – For generating interactive financial line charts

- **Regular Expressions (re)** – To extract companies and years from user queries

- **Base64** – For dynamic background image loading

- **CSV** – As the data source for financial metrics

- **HTML & CSS** (injected via Streamlit) – To style and personalize the UI with logos, text boxes, and themes

**Project Use**

 This chatbot simplifies financial analysis by offering:
- Instant access to historical and recent financial data of companies.
- Natural language interaction for ease of use (e.g., “Tesla revenue in 2023”).
- Visual financial insights via dynamic line charts.
- A user-friendly, stylish interface accessible via any browser.

**Methodology**

**1. Dataset Integration**

- Loads company financial data from a CSV file.
- Cleans columns (Revenue, Net Income, Assets) by removing special characters and ensuring numeric formats.

**2. NLP-Based Query Processing**

- Extracts company names and years from user input using string matching and regex.
- Maps flexible keywords (e.g., “sales”, “turnover” → revenue) to specific financial metrics using a predefined dictionary.

**3. Chatbot Logic**

- Matches queries against cleaned and structured data.
- Returns textual financial insights such as:
  “Apple total revenue in 2022: $394,328.00”
- If a valid metric and company are matched, it proceeds to chart generation.

**4. Data Visualization**

- Generates a dynamic Altair line chart for the requested metric over multiple years.
- Tooltip-enabled chart shows financial trends visually to the user.

**5. Streamlit Web Application**

- Welcome dashboard with chatbot usage instructions.
- Financial chatbot interface with real-time query input.

**Advantages**

- Natural Language Querying – No need to remember exact database terms; the chatbot handles variations like “profit” vs “net income”. Interactive Charts – Visualize company performance trends over time.
- Interactive Charts – Visualize company performance trends over time.
- Web-Based Interface – Easy to deploy and access from anywhere.
- Modular Design – Easy to extend for more companies, metrics, or predictive insights.
- User-Centric UI – Clean, responsive layout with intuitive navigation.
