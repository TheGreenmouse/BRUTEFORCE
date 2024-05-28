# BRUTEFORCE
 Brute forcing script.

 ## Arguments
```
--loginurl : The URL of the login page
--usernamesfile : The file list of usernames
--passwordsfile : The file list of passwords
--ntlm : Use NTLM authentication
--domain : The domain for NTLM authentication (if applicable)
```

## Examples
```
python bruteforce.py --loginurl http://files.example.com/ --usernamesfile usernames.txt --passwordsfile  passwords.txt --ntlm --domain example.com
```
