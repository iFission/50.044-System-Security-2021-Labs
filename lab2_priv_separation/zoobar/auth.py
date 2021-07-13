from zoodb import *
from debug import *

import hashlib
import random
import pbkdf2
import os

# -- Move to auth service -- apparently no need and idk why lol
def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

# -- Move to auth service
def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
   
    if not cred:
        return None
    # Modified for Task 6
    if cred.password == pbkdf2.PBKDF2(password, cred.salt).hexread(32):
        return newtoken(db, cred)
    else:
        return None

# -- Move to auth service
def register(username, password):
    db_person = person_setup()
    db_cred = cred_setup()
    
    person = db_person.query(Person).get(username)
    if person:
        return None
    # Create Person
    newperson = Person()
    newperson.username = username
    # Create the cred - Modified for Task 6
    salt = os.urandom(8).encode('base-64') # 64 bit salt, not a unicode string - so encode as b64
    password_hash = pbkdf2.PBKDF2(password, salt).hexread(32)
    newcred = Cred()
    newcred.password = password_hash
    newcred.username = username
    newcred.salt = salt
    # Commit changes
    db_person.add(newperson)
    db_cred.add(newcred)
    db_person.commit()
    db_cred.commit()

  
    
    return newtoken(db_cred, newcred)

# -- Move to auth service
def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

