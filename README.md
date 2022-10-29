# test_task
This repository contains some code for test task for tester position

------------

Task
----

Using the Python 3 language, write a script and check that:
1) Site https://sstmk.ru works
2) Find out the ip address of the host sstmk.ru
3) Find out the phone number of the company using a GET request to the main page of the site
4) Check the company's phone number for validity according to the following standard: +A(BBB)CCC-CC-CC, 
where A is the country code, from one to three digits (this part of the number is optional); 
ВВВ - city or zone code (the number of digits may be different from three);   
CCC-CC-CC - phone number (the number of digits may be different from seven).   
Examples of valid numbers: +7(495)222-22-22, (495)222-22-22, (34111)2-22-22.   
Output to stdout the phone number of the company according to the standard above.

Files
-----

[main.py](main.py) contains main program code. Task items are separated by '''number of item'''   
[requirements.txt](requirements.txt) contains a list of packages required for installation

----------------

You need install all requirements before start by next command:

    ```bash
    pip3 install -r path_to_file\requirements.txt
    ```
