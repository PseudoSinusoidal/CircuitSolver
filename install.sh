#!/bin/bash

# Stop for all errors
set -e

# Install Location
INSTALL_DIR="$HOME/.local/share/circuitsolver"

# Check if there's an old install
if [[ -d "$INSTALL_DIR" ]]; then
	# Ask installer
	echo "[!] CircuitSolver was found on your device. Would you like to replace the old one?"
	echo "[!] Warning: Not removing the previous version can cause unexpected behaviors!"
	read -p "[?] Replace? (Y/N) " install_answer < /dev/tty

	if [[ "$install_answer" == "Y" ]]; then
		rm -rf "$INSTALL_DIR" # Remove old directory

	elif [[ "$install_answer" == "N" ]]; then

	# Invalid
	else
		echo '[!] Invalid answer, please retry.'
		exit 1

	fi
fi

mkdir -p "$INSTALL_DIR" # Add new directory

# Remove any old install temp stuff
rm -f /tmp/cs.tar.gz
rm -rf /tmp/CircuitSolver-*

# Download the repo tarball to /tmp
curl -fsSL https://github.com/PseudoSinusoidal/CircuitSolver/archive/refs/heads/cli.tar.gz -o /tmp/cs.tar.gz

# Extract it into /tmp
tar -xzf /tmp/cs.tar.gz -C /tmp

# Copy extracted files into install directory
cp -r /tmp/CircuitSolver-*/* "$INSTALL_DIR"

echo "Thank you for choosing CircuitSolver."
echo "The program has been installed to $INSTALL_DIR"