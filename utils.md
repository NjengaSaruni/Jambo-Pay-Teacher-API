# To prevent pkg-resources from being added onto pip-freeze

    pip freeze | grep -v "pkg-resources" > requirements.txt

# To enter postgres shell

    sudo -su postgres psql shell