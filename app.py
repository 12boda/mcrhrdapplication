@st.cache_data
def load_data():
    df = pd.read_excel("All India National Family Health Survey1.xlsx")
    return df
