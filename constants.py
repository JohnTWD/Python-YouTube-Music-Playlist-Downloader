import os;

homeDir: str = os.getcwd();
baseUrl: str = "https://pipedapi.kavin.rocks";

def setBaseUrl(newLink: str) -> None:
    baseUrl = newLink;