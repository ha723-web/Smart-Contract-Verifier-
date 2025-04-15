import streamlit as st
from analyzer.ai_analyzer import analyze_with_llm
from analyzer.slither_checker import run_slither_check
from analyzer.utils import load_contract_code

st.set_page_config(page_title="AI-Powered Smart Contract Verifier")
st.title("🔐 AI-Powered Smart Contract Verifier")

st.markdown("""
Upload a Solidity smart contract file or paste the code below. Our AI engine and vulnerability scanner will review the contract and provide insights.
""")

contract_code = ""

upload = st.file_uploader("📤 Upload Solidity File (.sol)", type=["sol"])
if upload:
    contract_code = upload.read().decode("utf-8")
else:
    contract_code = st.text_area("✍️ Or Paste Solidity Code Here:", height=300)

if st.button("🔎 Analyze Contract") and contract_code:
    with st.spinner("Analyzing with AI and static tools..."):
        llm_response = analyze_with_llm(contract_code)
        slither_report = run_slither_check(contract_code)

    st.subheader("📄 AI Summary and Suggestions")
    st.write(llm_response)

    st.subheader("🛡️ Vulnerability Report (Static Analysis)")
    st.text(slither_report)