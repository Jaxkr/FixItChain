from prompt import *
from neo.Prompt.Commands.BuildNRun import BuildAndRun, LoadAndRun

settings.setup_privnet()
path = "privnet1"
Wallet = UserWallet.Open(path, to_aes_key("123123123123"))

BuildAndRun(['/Users/jacksonroberts/Desktop/TicketChain/test/RegisterPart.py', 'test', '020707', '07', 'True', 'False', '1', '5', '2'], Wallet)


print("hi there")