import shutil
import os

REQUIRED_TOOLS = ["forge"]
REQUIRED_ENV_VARS = ["ETHERSCAN_API_KEY"]

def check_environment():
    missing_tools = [tool for tool in REQUIRED_TOOLS if shutil.which(tool) is None]
    missing_env = [var for var in REQUIRED_ENV_VARS if os.getenv(var) is None]

    if missing_tools:
        print(f"❌ Missing CLI tools: {', '.join(missing_tools)}")
        print("👉 Example: Install Foundry via:")
        print("   curl -L https://foundry.paradigm.xyz | bash && foundryup")
    if missing_env:
        print(f"❌ Missing environment variables: {', '.join(missing_env)}")
        print("👉 Set them using export or a .env file.")
        print("   Example: export ETHERSCAN_API_KEY=your_key")

    return not (missing_tools or missing_env)
