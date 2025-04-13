#!/bin/bash

echo "Check if the virtual environment is activated"

if [[ -z "$VIRTUAL_ENV" ]]; then
  echo "Virtual environment not activated. Activating..."

  source backend/env/bin/activate
fi

echo "Checking for new packages..."

pip freeze > backend/requirements.txt

echo "Updating requirements.txt"

git add backend/requirements.txt

echo "Updated requirements.txt"
