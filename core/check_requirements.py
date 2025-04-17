import shutil
import sys
import os

REQUIRED_CLI_TOOLS = ["slither", "forge"]
REQUIRED_ENV_VARS = ["ETHERSCAN_API_KEY"]

def check_cli_tools():
    missing = []
    for tool in REQUIRED_CLI_TOOLS:
        if shutil.which(tool) is None:
            missing.append(tool)
    return missing

def check_env_vars():
    missing = []
    for var in REQUIRED_ENV_VARS:
        if var not in os.environ:
            missing.append(var)
    return missing

def run_full_check():
    print("🔍 Checking environment requirements...")

    cli_missing = check_cli_tools()
    env_missing = check_env_vars()

    if cli_missing:
        print(f"❌ Missing CLI tools: {', '.join(cli_missing)}")
        print("👉 Please install the above tools and ensure they are in your PATH.")
        print("   Examples:")
        if "slither" in cli_missing:
            print("   • Install Slither: pipx install slither-analyzer")
        if "forge" in cli_missing:
            print("   • Install Foundry: curl -L https://foundry.paradigm.xyz | bash && foundryup")

    if env_missing:
        print(f"❌ Missing environment variables: {', '.join(env_missing)}")
        print("👉 Please set them in your terminal or in a .env file.")
        print("   Example:")
        print("   export ETHERSCAN_API_KEY=your_key_here")

    if cli_missing or env_missing:
        sys.exit("🔒 Environment not ready. Exiting BugForce...")

    print("✅ All system checks passed. Let’s gooo! 🚀")
