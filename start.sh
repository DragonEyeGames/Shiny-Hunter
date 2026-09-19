echo "Pulling code from Git..."
git pull origin main

echo "Activating Venv..."
source venv/bin/activate

echo "Running Command"
sudo venv/bin/python3 main.py