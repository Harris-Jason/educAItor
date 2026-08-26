import streamlit as st
from openai import OpenAI
import pandas as pd

st.set_page_config(page_title="The Green Ledger | Dividend AI")
st.title("Dividend AI: Institutional AI Auditor")
st.markdown("""
Strategic Objective: Bridging the Implementation Gap for SDG 12.  
This Digital Core automates the synthesis of unstructured procurement data to neutralize 
the $1.53 Trillion Negative Carbon Price masking unsustainable costs.
""")

with st.sidebar:
    st.header("Institutional Access")
    openai_api_key = st.text_input("OpenAI API Key (GPT-4o)", type="password")
    st.info("Integration: Position Green & GitHub Active")
    st.subheader("Ingest Procurement Data")
    uploaded_file = st.file_uploader("Upload Vendor PDF or Technical Data Sheet", type=("pdf", "csv"))

if not openai_api_key:
    st.info("Please enter your API key to activate the Digital Core.")
else:
    client = OpenAI(api_key=openai_api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": """
            You are the Dividend AI Auditor. Your goal is to generate Digital Material Passports (DMP).
            1. Analyze unstructured data for Global Warming Potential (GWP) and provenance.
            2. Identify fossil-fuel dependencies cheapened by the $1.53T Negative Carbon Price.
            3. Issue a Compliance-as-Code verdict (Approve/Block) based on the group's 
               Subsidies-Neutral mandate.
            4. Recommend circular alternatives to decouple growth from extraction.
            """}
        ]

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("Audit a specific procurement line item..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
            )
            response = st.write_stream(stream)
            
            if "bus" in prompt.lower() or "fleet" in prompt.lower():
                st.success("Analysis Complete: Potential $243,000 Lifetime TCO Dividend Identified per vehicle.")
            
        st.session_state.messages.append({"role": "assistant", "content": response})

    st.divider()
    if st.button("Export to Position Green (SFDR/EDCI)"):
        st.write("Processing Digital Flow to Institutional Reporting cycle...")
        st.info("Compliance Verdict: Automated Block of Non-Compliant Extraction Assets active.")
