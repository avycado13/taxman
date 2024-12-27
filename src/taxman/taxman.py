import tomllib
from pypdf import PdfReader

# Get Config from toml file
with open("taxman.toml", "rb") as config_file:
    config:dict = tomllib.load(config_file)



