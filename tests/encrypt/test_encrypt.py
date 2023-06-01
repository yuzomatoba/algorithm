# from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Testando key e message incorretos:
    try:
        encrypted_message(231, 'Hey')
    except exception as ex:
        assert type(ex).__name__ == 'TypeError'

    # Testando que key não é um índice válido de message:
    assert encrypted_message(6, 'Hey') == 'yeH'
    assert encrypted_message(12, 'Hey') == 'yeH'

    # Testando se key é ímpar:
    assert encrypted_message(3, 'Hey') == 'H_ey'
    assert encrypted_message(5, 'Friend') == 'r_eiFn'

    # Testando se key é par:
    