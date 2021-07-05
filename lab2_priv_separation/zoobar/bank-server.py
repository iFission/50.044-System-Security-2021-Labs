#!/usr/bin/env python2
#
# Insert bank server code here.
#
import rpclib
import sys
import bank
from debug import *

class BankRpcServer(rpclib.RpcServer):
    ## Fill in RPC methods here.
    def rpc_transfer(self,sender, recipient, zoobars):
        return bank.transfer(sender, recipient, zoobars)

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
        res  = bank.get_log(username) # this function is crashing, with error that data is not a JSON - suspect is rpc issue
        return str(res) 

    def rpc_initalise_zoobars(self, username):
        return bank.initalise_zoobars(username)

(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
