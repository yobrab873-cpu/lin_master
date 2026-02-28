#!/bin/bash

# Create the launcher script
cat << EOF > /usr/local/sbin/lin
#!/bin/bash
python3 /home/Lin_master/main.py
EOF


chmod +x /usr/local/sbin/lin
echo "Launcher script created at /usr/local/sbin/lin"

# Install colorama
echo "Installing Python colorama..."
if sudo apt install -y python3-colorama; then
    echo "colorama installed successfully via apt"
else
    echo "apt install failed, trying pip3..."
    if pip3 install colorama; then
        echo "colorama installed successfully via pip3"
    else
        echo "Failed to install colorama. Please install manually."
    fi
fi

# Install figlet
echo "Installing figlet..."
if sudo apt install -y figlet; then
    echo "figlet installed successfully"
else
    echo "Failed to install figlet. Please install manually."
fi


echo "Setup completed!"
clear 
echo "TO START LINUX MASTER JUST TYPE < lin > IN YOUR LINUX COMMAND LIME"
