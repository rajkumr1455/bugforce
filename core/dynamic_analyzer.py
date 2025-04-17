import subprocess

def run_dynamic_analysis(source_code):
    try:
        print("⚙️ Running Foundry tests...")
        with open("test_contract.sol", "w") as f:
            f.write(source_code)
        
        # Initialize forge (skip if already initialized)
        subprocess.run(["forge", "init", "--force"], check=True)

        # Compile & test
        subprocess.run(["forge", "test"], check=True)
        
        return "✅ Foundry testing completed."
    except Exception as e:
        print(f"❌ Foundry testing failed: {str(e)}")
        return f"Foundry Error: {str(e)}"
