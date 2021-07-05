#!/usr/bin/env python2
#
# Insert bank server code here.
#
import rpclib
import sys
import bank
from debug import *
import auth_client


def serialise(sql_obj):
    return {c.name: getattr(sql_obj, c.name) for c in sql_obj.__mapper__.columns}

class BankRpcServer(rpclib.RpcServer):
    ## Fill in RPC methods here.
    # TODO: Add authentication method here
    def rpc_transfer(self,sender, recipient, zoobars, token):
        # Exercise 8 - Authenticate the request via token
        if not auth_client.check_token(sender, token):
            log("Transfer authentication failed") 
            raise ValueError('Token is invalid')

        return bank.transfer(sender, recipient, zoobars)

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        
        res  = bank.get_log(username) # this function is crashing, with error that data is not a JSON - suspect is rpc issue
        return res

    def rpc_initalise_zoobars(self, username):
        return bank.initalise_zoobars(username)

(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
