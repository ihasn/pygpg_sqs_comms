This is just me testing a chat/file transfer app via python.

Additional python module needed is gnupg.  pip install gnupg to set it up

To operate use the follow:

$ python sqs.py

*Enter your AWS Access key*
AWS Access key: ******************

*Enter your AWS Secret key*
AWS Secret key: ***********************************

*Enter gnupg homedir*
Type gpg home dir: /home/gnupghome/.gnupg

*Select option, send to send a message*
Please enter option(send, recieve, quit): send

*Available public keys are printed*
[{'dummy': u'', 'keyid': u'598D88714AB0262C', 'expires': u'', 'subkeys': [[u'FA5EDB364356E1', u'e']], 'length': u'2048', 'ownertrust': u'-', 'algo': u'1', 'fingerprint': u'9BB5DF4DF416D160C966CE3C598D88714AB0262C', 'date': u'1406814964', 'trust': u'-', 'type': u'pub', 'uids': [u'Patrick Pierson <*****@*******>']}]

*Enter your gpg key id*
GPG Key ID: 598D88714AB0262C

*Enter your message*
Message: this is a test

*Message is encrypted and sent to SQS*
Encrypted Message Send to SQS: -----BEGIN PGP MESSAGE-----

hQEMA/pd2zUpaWbhAQf7BtpXS1a8iuva9+05YtmcS0pynhi2rblPU7cIGgS7VDAH
A0FpoLKVvYQVOUhWFhKpI0GanZH7k0jlVGk/kdMqaHoycN3O5dbBrP/E0iJv9OmU
GyvaeKBT2tQT0tEp1qo4dFVyMHJyp32jQArVyozRT8DH2rqZdfGdeeBO9gY/eclv
RyXAg+3IeLG6tWN9Cfgo/9oCcGdQGxcISlAjmDiYi2jhUzTBL9JdPNtzZKP3joH+
Wawldsjlsajl4wjt20t28ugf20v0rWKSGKWEKHJ231KlewkjflsjadflaswqeSLJ
4R/JxDUX/xuUT9kawXFS2LHwB9J30H94tzrIJq7R0d8eIqQ8ZzcON160FEDp3R3d
tXXGTmPQMINXYCDhzRTcNKnd7sO1bCkvT7YArtM2MNb3R0omWdrVLv3EyGktYdPT
6w9eVgIiQTKi
=bEkE
-----END PGP MESSAGE-----

*Select option, recieve to recieve a message*
Please enter option(send, recieve, quit): recieve

*Available private keys are printed*
[{'dummy': u'', 'keyid': u'598D88714AB0262C', 'expires': u'', 'subkeys': [], 'length': u'2048', 'ownertrust': u'', 'algo': u'1', 'fingerprint': u'9BB5DF4DF416D160C966CE3C598D88714AB0262C', 'date': u'1406814964', 'trust': u'', 'type': u'sec', 'uids': [u'Patrick Pierson <********@**********>']}]

*Enter your gpg key id*
GPG Private ID: 598D88714AB0262C

*Enter your password*
Password: ****************

*Message is returned from SQS, still encrypted.*
Pulled Encrypted Message: -----BEGIN PGP MESSAGE-----

hQEMA/pd2zUpaWbhAQf7BtpXS1a8iuva9+05YtmcS0pynhi2rblPU7cIGgS7VDAH
A0FpoLKVvYQVOUhWFhKpI0GanZH7k0jlVGk/kdMqaHoycN3O5dbBrP/E0iJv9OmU
GyvaeKBT2tQT0tEp1qo4dFVyMHJyp32jQArVyozRT8DH2rqZdfGdeeBO9gY/eclv
RyXAg+3IeLG6tWN9Cfgo/9oCcGdQGxcISlAjmDiYi2jhUzTBL9JdPNtzZKP3joH+
Wawldsjlsajl4wjt20t28ugf20v0rWKSGKWEKHJ231KlewkjflsjadflaswqeSLJ
4R/JxDUX/xuUT9kawXFS2LHwB9J30H94tzrIJq7R0d8eIqQ8ZzcON160FEDp3R3d
tXXGTmPQMINXYCDhzRTcNKnd7sO1bCkvT7YArtM2MNb3R0omWdrVLv3EyGktYdPT
6w9eVgIiQTKi
=bEkE
-----END PGP MESSAGE-----

*Message is decrypted and printed*
Decrypted Message: this is a test

*Select option, quit to quit out.*
Please enter option(send, recieve, quit): quit
