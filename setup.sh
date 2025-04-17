#!/bin/bash

echo "🔧 Setting up BugForce CLI Environment..."

# Step 1: Python virtual environment (optional but good practice)
if [ ! -d "venv" ]; then
  echo "📦 Creating Python virtual environment..."
  python3 -m venv venv
fi

source venv/bin/activate

# Step 2: Install Python dependencies
echo "📥 Installing Python dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 3: Install Slither using pipx
if ! command -v slither &> /dev/null; then
  echo "🐍 Installing Slither Analyzer..."
  pip install pipx
  pipx ensurepath
  pipx install slither-analyzer
else
  echo "✅ Slither is already installed."
fi

# Step 4: Install Foundry
if ! command -v forge &> /dev/null; then
  echo "🔨 Installing Foundry..."
  curl -L https://foundry.paradigm.xyz | bash
  source ~/.bashrc
  foundryup
else
  echo "✅ Foundry is already installed."
fi

# Step 5: Create .env file if not exists
if [ ! -f ".env" ]; then
  echo "📝 Creating .env file..."
  cat <<EOF > .env
# Add your Etherscan API key below
ETHERSCAN_API_KEY=your_key_here
EOF
  echo "⚠️  Don't forget to replace 'your_key_here' with your actual Etherscan API key!"
else
  echo "✅ .env file already exists."
fi

echo "🎉 Setup complete! You can now run:"
echo ""
echo "  source venv/bin/activate"
echo "  python bugforce.py --smartcontract 0xYourTargetHere --network ethereum"
echo ""
