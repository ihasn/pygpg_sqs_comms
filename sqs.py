import boto.sqs, gnupg, getpass, time, urllib

from boto.sqs.message import Message

use_local_boto = raw_input("Use local AWS keys? (yes or no)")
if use_local_boto == 'no':
  aws_access_key_id = raw_input("AWS Access key: ")
  aws_secret_access_key = raw_input("AWS Secret key: ")
  conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
else:
  conn = boto.sqs.connect_to_region("us-east-1")
homedir_loc = raw_input('Type gpg home dir: ')
gpg = gnupg.GPG(binary='/usr/bin/gpg2', homedir=homedir_loc)

while True:
    n = raw_input("Please enter option(send, recieve, search, quit): ")
    if n.strip() == 'quit':
        break
    if n.strip() == 'send':
        print gpg.list_keys()
        key_id_queue = raw_input("GPG Key ID: ")
        q = conn.create_queue(key_id_queue)
        m = Message()
        message = raw_input("Message: ")
        encrypt_message = str(gpg.encrypt(message, key_id_queue))
        print "Encrypted Message Send to SQS: " + encrypt_message
        m.set_body(encrypt_message)
        q.write(m)
    if n.strip() == 'recieve':
        print gpg.list_keys(True)
        key_id_queue = raw_input("GPG Private ID: ")
        password = getpass.getpass()
        q = conn.get_queue(key_id_queue)
        rs = q.get_messages()
        m = rs[0]
        pulled_encrypt_message = m.get_body()
        print "Pulled Encrypted Message: " + pulled_encrypt_message
        decrypted_message = str(gpg.decrypt(str(pulled_encrypt_message), passphrase=password))
        if decrypted_message == '':
          print "Posting back to SQS, incorrect key or password"
          q.write(m)
        else:
          print "Decrypted Message: " + decrypted_message
        
    if n.strip() == 'search':
        search = raw_input("Search for: ")
        response = urllib.urlopen("http://pgp.mit.edu:11371/pks/lookup?options=mr&op=get&search=" + search)
        pub_key = response.read()
        from pgpdump import AsciiData
        test = AsciiData(pub_key)
        test.strip_magic(pub_key)
        packets = list(test.packets())
        print packets[1]
        add_response = raw_input("Add this Pubkey? (yes or no) ")
        if add_response == 'yes':
          print "Import: ", gpg.import_keys(pub_key).summary()
        else:
          print "Returning"


#conn.delete_queue(q)
