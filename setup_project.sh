#!/usr/bin/env bash
./scripts/make_environment.sh
source ./env/bin/activate
./scripts/install_python_requirements.sh
cp ./src/app/local_settings.py.development ./src/app/local_settings.py
mkdir ./data/ && ./scripts/sync_db.sh
echo ""
echo "Now go to http://127.0.0.1:3000/ to check if everything works."
echo "...and please, don't add debugging middlewares and other crap."
echo "Use ipdb and prints"
./scripts/run_project.sh
