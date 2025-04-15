# 🔐 AI-Powered Smart Contract Verifier

This project is a decentralized application (dApp) built with **Streamlit** and **LLMs (OpenAI GPT)** that analyzes Solidity smart contracts for vulnerabilities and suggests improvements using both AI and static analysis tools like **Slither**.

## 🚀 Features
- Upload or paste Solidity smart contract code
- LLM-generated review and suggestions
- Vulnerability scanning using Slither
- Clear output and downloadable insights

## 🧰 Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python, Web3.py
- **AI Engine:** OpenAI GPT-3.5
- **Static Analysis:** Slither

## 📦 Installation
```bash
git clone https://github.com/yourusername/SmartContractVerifier.git
cd SmartContractVerifier
pip install -r requirements.txt
```

## 🔑 Setup API Key
Create a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## ▶️ Run the App
```bash
streamlit run app.py
```

## 📂 Folder Structure
```
SmartContractVerifier/
├── analyzer/
│   ├── ai_analyzer.py
│   ├── slither_checker.py
│   └── utils.py
├── samples/
│   ├── good_contract.sol
│   └── vulnerable_contract.sol
├── app.py
├── requirements.txt
└── README.md
```

## 📜 License
MIT

## 📂 Commands to Run
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
touch .env
OPENAI_API_KEY=your_openai_key_here
streamlit run app.py

```
