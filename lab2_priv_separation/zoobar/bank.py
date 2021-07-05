from zoodb import *
from debug import *

import time

def transfer(sender, recipient, zoobars):
    # Exercise 7 - Swapped to bankDB
    bankdb = bank_setup()
    senderp = bankdb.query(Bank).get(sender)
    recipientp = bankdb.query(Bank).get(recipient)

    sender_balance = senderp.zoobars - zoobars
    recipient_balance = recipientp.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    senderp.zoobars = sender_balance
    recipientp.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    db = bank_setup()
    person = db.query(Bank).get(username)
    return person.zoobars

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))


# Exercise 7 - Added interface for initialisation of zoobars

def initalise_zoobars(username):
    db = bank_setup()
    person = db.query(Bank).get(username)
    # If somehow a profile doesnt exist but a bank entry exist, somehting is seriously wrong
    if person:
        return None
    newbankentry = Bank()
    newbankentry.username = username
    # no need to initialise zoobars, SQL handle by default
    db.add(newbankentry)
    db.commit()

