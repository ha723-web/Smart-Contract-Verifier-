def load_contract_code(path: str) -> str:
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Failed to load file: {e}"