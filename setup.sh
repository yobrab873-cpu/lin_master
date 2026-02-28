#!/bin/bash
# setup_debug.sh - Debug-first-time setup for LIN_MASTER
# Author: Brian Njuguna
# Purpose: Ensure smooth first-time installation

# ====== BASE DIR ======
BASE_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "LIN_MASTER Setup - Debug Version"
echo "Base directory: $BASE_DIR"

# ====== Check dependencies ======
echo "Checking system dependencies..."

# Git
command -v git >/dev/null 2>&1 || {
    echo "Git not found, installing..."
    sudo apt update && sudo apt install -y git
}

# Figlet
command -v figlet >/dev/null 2>&1 || {
    echo "Figlet not found, installing..."
    sudo apt install -y figlet
}

# Python3 and pip
command -v python3 >/dev/null 2>&1 || {
    echo "Python3 not found, please install Python3 first!"
    exit 1
}

python3 -m pip --version >/dev/null 2>&1 || {
    echo "pip3 not found, installing..."
    sudo apt install -y python3-pip
}

# Python modules
echo "Installing Python modules..."
python3 -m pip install --upgrade pip
python3 -m pip install colorama

# ====== Create launcher script ======
LAUNCHER="$HOME/bin/lin"

mkdir -p "$HOME/bin"

cat << EOF > "$LAUNCHER"
#!/bin/bash
python3 "$BASE_DIR/main.py"
EOF

chmod +x "$LAUNCHER"
echo "Launcher created: $LAUNCHER"
echo "Make sure ~/bin is in your PATH"

# ====== Check zphisher folder ======
ZPHISHER="$BASE_DIR/zphisher"
if [ ! -d "$ZPHISHER" ]; then
    echo "zphisher not found, cloning..."
    git clone https://github.com/htr-tech/zphisher.git "$ZPHISHER"
else
    echo "zphisher already exists."
fi

echo "Setup completed! You can now run LIN_MASTER with: lin"
