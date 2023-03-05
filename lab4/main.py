from lab4.core.controller import Controller

from lab4.cli.Application import Application
from lab4.cli.CommandHandler import CommandHandler

from lab4.cli.handlers import account_info
from lab4.cli.handlers import insert_card
from lab4.cli.handlers import input_pincode
from lab4.cli.handlers import phone_payment_operation
from lab4.cli.handlers import transfers_info
from lab4.cli.handlers import withdrawal_operation
from lab4.cli.handlers import get_card

from lab4.gui.Application import Application


def cli():
    app = Application(Controller())
    app.add_handler(CommandHandler(('c:', 'card='), insert_card))
    app.add_handler(CommandHandler(('p:', 'pin='), input_pincode))
    app.add_handler(CommandHandler(('i', 'info'), account_info))
    app.add_handler(CommandHandler(('t', 'transfers'), transfers_info))
    app.add_handler(CommandHandler(('w:', 'withdraw='), withdrawal_operation))
    app.add_handler(CommandHandler(('o:', 'phone='), phone_payment_operation))
    app.add_handler(CommandHandler(('g', 'get_card'), get_card))
    app.add_root_handler(lambda : print('USAGE'))
    app.start()


def gui():
    app = Application(Controller())
    app.run()

    