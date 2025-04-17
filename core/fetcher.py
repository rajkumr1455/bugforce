import requests
import os

def fetch_contract(address, network):
    api_base = {
        "eth": "https://api.etherscan.io/api",
        "bsc": "https://api.bscscan.com/api",
        "polygon": "https://api.polygonscan.com/api"
    }

    if network not in api_base:
        raise Exception(f"Unsupported network: {network}")

    API_KEY = os.getenv("ETHERSCAN_API_KEY")
    url = f"{api_base[network]}?module=contract&action=getabi&address={address}&apikey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    print(f"📦 BscScan API Response: {data}")

    if data["status"] != "1":
        raise Exception("Failed to fetch contract data: " + data.get("result", "Unknown error"))

    return data["result"]
