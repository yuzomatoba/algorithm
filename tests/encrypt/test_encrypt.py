from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = 'butterfly'

    with pytest.raises(TypeError, match='inválido o tipo de key'):
        encrypt_message(message, None)

    with pytest.raises(TypeError, match='inválido o tipo de message'):
        encrypt_message(None, 0)
   
    assert encrypt_message(message, 0) == 'flybutter'

    assert encrypt_message(message, 1) == 'f_ylbtture'

    assert encrypt_message(message, 2) == 'btterul_yf'