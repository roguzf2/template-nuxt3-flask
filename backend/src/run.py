""" Module that starts the server """
# Standard libraries
from os import getenv

# Local imports
from src.server import server

if __name__ == "__main__":
    server.run(
        host=getenv("HOST", "localhost"),
        port=getenv("PORT", "5000"),
        debug=int(getenv("DEBUG", 1)) == 1
    )
