import subprocess
import tempfile

def run_static_analysis(contract_abi):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        temp_file.write(contract_abi.encode("utf-8"))
        temp_file.flush()

        try:
            result = subprocess.run(["slither", temp_file.name], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"Slither failed: {str(e)}"
