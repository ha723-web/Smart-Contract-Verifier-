import subprocess
import tempfile
import os

def run_slither_check(code: str) -> str:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".sol", mode='w') as tmp:
            tmp.write(code)
            tmp_path = tmp.name

        result = subprocess.run(["slither", tmp_path], capture_output=True, text=True, timeout=30)
        os.remove(tmp_path)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Slither failed: {e}"
    