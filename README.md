# Google Calendar API test

Test Google Calendar API

## Setup

1. Register Google API account
2. Create new project
3. Go to credentials page: https://console.developers.google.com/apis/credentials
4. Create credentials-->OAuth client ID
5. Application type: Web application
6. Create
7. Authorized redirect URIs: http://localhost:8080/
8. Save
9. Download JSON
10. Save JSON to project folder as `client_secrets.json`, keep content of that file in secret

## Installation

Run on a local PC:

```bash
. env/bin/activate
pip3 install -r requirements.txt
pytest
```

You have to grant access to the application manually for the first time in the web browser page

## Supported Python Versions

Python 3.7 is fully supported and tested.
