#!/bin/bash

echo "Checking for new packages..."
pip freeze > backend/requirements.txt
git add backend/requirements.txt
echo "Updated requirements.txt"
