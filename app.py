import streamlit as st
import pandas as pd
import altair as alt
import re
import base64

# --- Load & Clean Data ---
df = pd.read_csv("financial.csv")

def clean_column(col):
    return col.replace('[\n\t,]', '', regex=True).replace('', '0').astype(float)

df["Total Revenue"] = clean_column(df["Total Revenue"])
df["Net Income"] = clean_column(df["Net Income"])
df["Total Assets"] = clean_column(df["Total Assets"])

# --- Flexible Chatbot Logic with Keyword Mapping ---
def simple_chatbot(user_input, df):
    user_input = user_input.lower()

    matched_companies = [c for c in df["Company"].unique() if c.lower() in user_input]
    matched_years = [int(y) for y in re.findall(r'\b(20\d{2})\b', user_input)]

    if not matched_companies:
        return "Sorry, I couldn't find a matching company.", None, None

    company = matched_companies[0]
    company_data = df[df["Company"].str.lower() == company.lower()]

    if matched_years:
        year = matched_years[0]
        company_data = company_data[company_data["Fiscal Year"] == year]
        if company_data.empty:
            return f"No data for {company} in {year}.", company, None
    else:
        company_data = company_data.sort_values("Fiscal Year")

    latest = company_data.iloc[-1]

    # Flexible keyword mapping
    metric_keywords = {
        "Total Revenue": ["revenue", "revenues", "sales", "turnover"],
        "Net Income": ["income", "net income", "profit", "earnings"],
        "Total Assets": ["asset", "assets", "total asset", "resources"]
    }

    matched_metric = None
    for metric, keywords in metric_keywords.items():
        if any(keyword in user_input for keyword in keywords):
            matched_metric = metric
            break

    if matched_metric:
        return f"{company} {matched_metric.lower()} in {latest['Fiscal Year']}: ${latest[matched_metric]:,.2f}", company, matched_metric
    else:
        return "Try asking about revenue, net income, or assets.", company, None

# --- Page Setup ---
st.set_page_config(page_title="Financial Chatbot", layout="wide")

# --- Session State Page Toggle ---
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# --- Choose Background for Page ---
bg_file = "welcome_bg.jpg" if st.session_state.page == "welcome" else "chat_bg.jpg"
with open(bg_file, "rb") as f:
    bg_base64 = base64.b64encode(f.read()).decode()

# --- Inject Fixed CSS ---
st.markdown(f"""
    <style>
    html {{
        height: 100%;
        background-image: url("data:image/jpg;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    body {{
        background-color: rgba(255, 255, 255, 0.85);
    }}
    .stApp {{
        background-color: transparent;
    }}
    .stTextInput > div > div > input {{
        background-color: #e8f0fe;
        color: #1a1a1a;
    }}
    .stButton > button {{
        background-color: #003366;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }}
    h1, h2, h3 {{
        color: #003366;
    }}
    </style>
""", unsafe_allow_html=True)

# --- Logo on Top Left ---
st.image("logo.png", width=150)

# --- Welcome Page ---
if st.session_state.page == "welcome":
    st.title("💼 Welcome to the Financial Insights Chatbot!")
    st.subheader("Get real-time insights about company finances.")

    st.markdown("""
    **Examples:**
    - `Tesla revenue in 2023`
    - `Apple net income`
    - `Microsoft assets in 2022`
    """)

    if st.button("Start Exploring"):
        st.session_state.page = "chat"

# --- Chatbot Page ---
elif st.session_state.page == "chat":
    st.title("📊 Financial Chatbot Dashboard")
    st.subheader("Ask about a company's revenue, income, or assets:")

    user_input = st.text_input("💬 Enter your question:")

    if user_input:
        response, company, metric = simple_chatbot(user_input, df)
        st.success(response)

        if company and metric:
            chart_data = df[df["Company"].str.lower() == company.lower()].sort_values("Fiscal Year")
            st.subheader(f"{company} - {metric} Over the Years")
            chart = alt.Chart(chart_data).mark_line(point=True).encode(
                x=alt.X("Fiscal Year:O", title="Year"),
                y=alt.Y(f"{metric}:Q", title=f"{metric} ($)", scale=alt.Scale(zero=False)),
                tooltip=["Fiscal Year", metric]
            ).properties(width=700, height=400)
            st.altair_chart(chart, use_container_width=True)

    if st.button("🔙 Go to Welcome Dashboard"):
        st.session_state.page = "welcome"
