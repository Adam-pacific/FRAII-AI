import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def generate_summary(df):
    st.subheader("🔍 Dataset Summary")
    st.write("🧮 Total Rows:", df.shape[0])
    st.write("🧮 Total Columns:", df.shape[1])
    st.write("🧼 Missing Values:", df.isnull().sum().sum())

    # Numeric stats
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols):
        st.subheader("📊 Numeric Stats")
        st.dataframe(df[numeric_cols].describe())

        for col in numeric_cols:
            st.write(f"📈 Distribution of **{col}**")
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            st.pyplot(fig)

    # Categorical summary
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols):
        st.subheader("📁 Top Categories")
        for col in cat_cols:
            st.write(f"Top in **{col}**:")
            st.dataframe(df[col].value_counts().head(5))
