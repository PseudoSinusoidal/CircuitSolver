#!/usr/bin/env bash
set -e

echo "Installing CircuitSolver..."

# remove old version
rm -rf "$HOME/CircuitSolver-cli"

# download + extract
curl -fsSL https://github.com/PseudoSinusoidal/CircuitSolver/archive/refs/heads/cli.tar.gz | tar -xz -C "$HOME"

# create command
mkdir -p "$HOME/.local/bin"

echo '#!/usr/bin/env bash
cd "$HOME/CircuitSolver-cli"
python3 -m circuitsolver.main "$@"' > "$HOME/.local/bin/circuitsolver"

chmod +x "$HOME/.local/bin/circuitsolver"

echo "Done! Run: circuitsolver"