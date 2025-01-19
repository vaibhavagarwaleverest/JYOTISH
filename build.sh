curl -sSL https://dot.net/v1/dotnet-install.sh | bash /dev/stdin --version 7.0.20 --install-dir /opt/render/project/src/.dotnet

# Add .NET to PATH
export PATH="$PATH:/opt/render/project/src/.dotnet"

# Install Python dependencies
pip install -r backend/requirements.txt