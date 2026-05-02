#!/bin/bash

# Stop for all errors
set -e

# Install Location
INSTALL_DIR="$HOME/.local/share/circuitsolver"

if [[ -d "$INSTALL_DIR" ]]; then
	echo "[!] CircuitSolver was found on your device. Would you like to replace the old one?"
	echo "[!] Warning: Not removing the previous version can cause unexpected behaviors!"
	read -p "[?] Replace? (Y/N) " install_answer

	if [[ "$install_answer" == "Y" ]]; then
		rm -rf "$INSTALL_DIR" # Remove old directory
		mkdir -p "$INSTALL_DIR" # Add new directory
	elif [[ "$install_answer" == "N" ]]; then
		mkdir -p "$INSTALL_DIR" # Add new directory
	else
		echo "[!] Invalid answer, please use "Y" or "N". "
	fi

# Download the repo tarball to /tmp
curl -fsSL https://github.com/PseudoSinusoidal/CircuitSolver/archive/refs/heads/cli.tar.gz -o /tmp/cs.tar.gz

# Extract it into /tmp
tar -xzf /tmp/cs.tar.gz -C /tmp

# Copy extracted files into install directory
cp -r /tmp/CircuitSolver-*/* "$INSTALL_DIR"

echo "Thank you for choosing CircuitSolver."
echo "The program has been installed to $INSTALL_DIR"