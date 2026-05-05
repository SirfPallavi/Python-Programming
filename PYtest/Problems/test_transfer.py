import pytest
from transfer import transfer, TransferError


# ✅ Successful transfer
def test_transfer_success():
    assert transfer("1234567890", "0987654321", 500, 1000) == 500


# ❌ Zero amount
def test_transfer_zero_amount():
    with pytest.raises(TransferError, match="Invalid transfer amount"):
        transfer("1234567890", "0987654321", 0, 1000)


# ❌ Insufficient balance
def test_transfer_insufficient_balance():
    with pytest.raises(TransferError, match="Insufficient balance"):
        transfer("1234567890", "0987654321", 1500, 1000)


# ❌ Invalid account number
def test_transfer_invalid_account():
    with pytest.raises(TransferError, match="Invalid account number"):
        transfer("12345", "0987654321", 500, 1000)