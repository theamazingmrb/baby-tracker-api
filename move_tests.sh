#!/bin/bash

# Copy all test files from tracker/tests to tracker directory
for file in tracker/tests/test_*.py; do
  cp "$file" tracker/
  echo "Copied $file to tracker/"
done

echo "All test files copied successfully"
