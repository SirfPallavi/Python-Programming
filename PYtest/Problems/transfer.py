import re

class TransferError(Exception):
    pass


def transfer(from_account, to_account, amount, balance):
    # Validate account number (10 digits)
    if not re.match(r"^\d{10}$", from_account) or not re.match(r"^\d{10}$", to_account):
        raise TransferError("Invalid account number")

    # Validate amount
    if amount <= 0:
        raise TransferError("Invalid transfer amount")

    # Validate balance
    if amount > balance:
        raise TransferError("Insufficient balance")

    return balance - amount