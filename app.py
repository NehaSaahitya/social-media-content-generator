import streamlit as st
import pandas as pd
from agent_logic import generate_social_media_content


# -----------------------------------------
# PAGE TITLE
# -----------------------------------------
st.title("🌟 Social Media Content Generator (AI Agent)")
st.write("Generate ideas, captions & templates for Instagram, LinkedIn, or Twitter/X.")

# -----------------------------------------
# USER INPUTS
# -----------------------------------------
topic = st.text_input("Enter a topic for content:")
platform = st.selectbox("Choose a platform:", ["Instagram", "LinkedIn", "Twitter/X"])

generate_btn = st.button("Generate Content")

# -----------------------------------------
# GENERATE OUTPUT
# -----------------------------------------
if generate_btn:
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        st.write("⏳ Generating content... please wait.")

        result = generate_social_media_content(topic, platform)

        st.subheader("Generated Content:")
        st.write(result)

        # -----------------------------------------
        # CSV DOWNLOAD
        # -----------------------------------------
        df = pd.DataFrame({"Content": [result]})

        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name="social_media_content.csv",
            mime="text/csv"
        )
