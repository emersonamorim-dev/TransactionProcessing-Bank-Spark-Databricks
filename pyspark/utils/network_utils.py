import requests
from typing import Dict, Optional, Union

def fetch_data_from_url(url: str) -> str:
    """Fetch data from a URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def post_data_to_url(url: str, data: Union[Dict, str], headers: Optional[Dict[str, str]] = None) -> str:
    """Send data to a URL."""
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.text

def download_file_from_url(url: str, destination: str) -> None:
    """Download a file from a URL and save it locally."""
    response = requests.get(url)
    response.raise_for_status()
    with open(destination, 'wb') as file:
        file.write(response.content)

def fetch_with_custom_headers(url: str, headers: Dict[str, str]) -> str:
    """Fetch data from a URL with custom headers."""
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def fetch_with_authentication(url: str, username: str, password: str) -> str:
    """Fetch data from a URL that requires authentication."""
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    return response.text

def fetch_with_parameters(url: str, params: Dict[str, str]) -> str:
    """Fetch data from a URL with query parameters."""
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


