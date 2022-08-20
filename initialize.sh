#!/bin/sh -e

if [ $# -eq 0 ]; then
  env_dir=env
else
  env_dir="$1"
fi

if [ ! -d "$env_dir" ]; then
  python3 -m venv "$env_dir"
fi

"$env_dir"/bin/pip install -r requirements.txt
