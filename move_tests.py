#!/usr/bin/env python
import os
import shutil

# Source and destination directories
source_dir = 'tracker/tests'
dest_dir = 'tracker'

# Get all Python files in the source directory
test_files = [f for f in os.listdir(source_dir) if f.endswith('.py') and f != '__init__.py']

# Copy each test file to the destination directory
for file_name in test_files:
    source_path = os.path.join(source_dir, file_name)
    dest_path = os.path.join(dest_dir, file_name)
    print(f"Copying {source_path} to {dest_path}")
    shutil.copy2(source_path, dest_path)

print(f"Successfully copied {len(test_files)} test files to {dest_dir}")
