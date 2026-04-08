import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("📊 AI A/B Test Interpreter")
mode = st.radio(
    "Choose analysis type:",
    ["Single Experiment", "Compare Variants"]
)

if st.button("Try Example"):
    user_input = "Improved onboarding, retention +5%, revenue -3%"

primary_metric = st.selectbox(
    "Select primary success metric:",
    ["Retention", "Revenue", "Conversion", "Engagement"]
)
if mode == "Single Experiment":
    st.write("To try out this application, try using these buttons:")

    # Initialize session state
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    
    col1, col2 = st.columns(2)

    if col1.button("Retention ↑ Revenue ↓"):
        st.session_state.user_input = "Improved onboarding, retention +5%, revenue -3%"

    if col2.button("Revenue ↑ Retention ↓"):
        st.session_state.user_input = "Added paywall, revenue +6%, retention -2%"

    # Input box (gets filled from session state)

    user_input = st.text_area(
        "Or describe your experiment and enter your A/B test result:",
        value=st.session_state.user_input
    )

if mode == "Single Experiment":
    #user_input = st.text_area("Describe your experiment and enter your A/B test result:")

    if st.button("Analyze"):
        if user_input:
            prompt = f"""
            You are a senior product analyst.

            A user ran an A/B test and got this result:
            "{user_input}"

            A user wants to focus on primary metric:
            "{primary_metric}"

            Focusing on the primary metric

            IMPORTANT:
            - Return ONLY valid JSON
            - Do NOT include any text before or after JSON
            - Do NOT use markdown (no ```)

            Return STRICT JSON:
            {{
                "summary": "...",
                "hypothesis": "...",
                "interpretation": "...",
                "metrics": ["...", "..."],
                "recommendation": "ship / iterate / rollback",
                "confidence": "low / medium / high"
            }}
            """

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            output = response.choices[0].message.content.strip()
            output = output.replace("```json", "").replace("```", "")

            try:
                data = json.loads(output)

                st.subheader("📌 Summary")
                st.write(data["summary"])

                st.subheader("🧠 Hypothesis")
                st.write(data["hypothesis"])

                st.subheader("📊 Interpretation")
                st.write(data["interpretation"])

                st.subheader("📈 Metrics to Check")
                for m in data["metrics"]:
                    st.write(f"- {m}")

                st.subheader("🔍 Confidence")
                st.write(data["confidence"])
                rec = data["recommendation"].lower()
                if "ship" in rec:
                    st.success("🚀 Ship")
                elif "iterate" in rec:
                    st.warning("🔁 Iterate")
                else:
                    st.error("⛔ Rollback")

            except Exception as e:
                st.error("JSON parsing failed")
                st.write(output)


elif mode == "Compare Variants":
        variant_a = st.text_area("Variant A result")
        variant_b = st.text_area("Variant B result")

        if st.button("Compare"):
            if mode == "Compare Variants":
                prompt = f"""
                You are a senior product analyst.

                Compare these two experiment results:

                Variant A:
                {variant_a}

                Variant B:
                {variant_b}

                Return STRICT JSON:

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

            output = response.choices[0].message.content.strip()
            output = output.replace("```json", "").replace("```", "")

            try:
                data = json.loads(output)

                st.subheader("🏆 Winner")
                st.write(data["winner"])

                st.subheader("🧠 Reason")
                st.write(data["reason"])

                st.subheader("⚠️ Risks")
                st.write(data["risks"])

                st.subheader("✅ Recommendation")
                st.write(data["recommendation"])

            except Exception as e:
                st.error("JSON parsing failed")
                st.write(output)

        else:
            st.warning("Please fill both variants.")
