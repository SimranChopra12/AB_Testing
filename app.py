import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("📊 AI A/B Test Interpreter")
mode = st.radio(
    "Choose analysis type:",
    ["Single Experiment", "Compare Variants"]
)
primary_metric = st.selectbox(
    "Select primary success metric:",
    ["Retention", "Revenue", "Conversion", "Engagement"]
)

if mode == "Single Experiment":
    user_input = st.text_area("Desribe your experiment and enter your A/B test result:")

    if st.button("Analyze"):
        if user_input:
            prompt = f"""
            You are a senior product analyst.

            A user ran an A/B test and got this result:
            "{user_input}"

            A user wants to focus on primary metric:
            "{primary_metric}"

            Focusing on the primary metric

            Return:
            - Hypothesis
            - Metric interpretation
            - Additional metrics to check
            - Recommendation
            """

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            st.write(response.choices[0].message.content)

elif mode == "Compare Variants":
        variant_a = st.text_area("Variant A result")
        variant_b = st.text_area("Variant B result")
        if st.button("Compare"):
            if mode == "Compare Variants" and variant_a and variant_b:
                prompt = f"""
                You are a senior product analyst.

                Compare these two experiment results:

                Variant A:
                {variant_a}

                Variant B:
                {variant_b}

                Return in JSON:

                {{
                "winner": "A or B",
                "reason": "...",
                "risks": "...",
                "recommendation": "ship A / ship B / iterate"
                }}
                """
                response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            st.write(response.choices[0].message.content)

        else:
            st.warning("Please fill both variants.")
