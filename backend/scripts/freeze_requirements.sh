#!/bin/bash

echo "Checking for new packages..."
pip freeze > requirements.txt
echo "Updated requirements.txt"
