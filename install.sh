#!/usr/bin/env bash
set -e

echo "Installing CircuitSolver..."

# clean old install
rm -rf "$HOME/CircuitSolver-cli"

# download correct branch
curl -fsSL https://github.com/PseudoSinusoidal/CircuitSolver/archive/refs/heads/cli.tar.gz | tar -xz -C "$HOME"

# rename extracted folder to stable name
rm -rf "$HOME/CircuitSolver-cli"
mv "$HOME/CircuitSolver-cli" "$HOME/CircuitSolver-cli"

# create command
mkdir -p "$HOME/.local/bin"

cat > "$HOME/.local/bin/circuitsolver" << 'EOF'
#!/usr/bin/env bash
cd "$HOME/CircuitSolver-cli"
python3 -m circuitsolver.main "$@"
EOF

chmod +x "$HOME/.local/bin/circuitsolver"

echo "Done! Run: circuitsolver"
