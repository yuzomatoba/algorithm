from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = 'butterfly'

    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message(message, None)

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(None, 0)

    assert encrypt_message(message, 0) == 'ylfrettub'

    assert encrypt_message(message, 1) == 'b_ylfrettu'

    assert encrypt_message(message, 2) == 'ylfrett_ub'
