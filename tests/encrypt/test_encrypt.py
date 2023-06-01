from challenges.challenge_encrypt_message import encrypt_message


# def encrypted_message(key, message):
#     if not isinstance(key, int) or not isinstance(message, str):
#         raise TypeError('key deve ser int e message deve ser do str')

#     if key < 0 or key >= len(message):
#         return message[::-1]

#     inverted_words = [message[:key], message[key:]]
#     if key % 2 == 0:
#         inverted_words.reverse()

#     encrypted_inverted_words = [word[::-1] for word in inverted_words]
#     encrypted_message = '_'.join(encrypted_inverted_words)

#     return encrypted_message
def test_encrypt_message():
    # Testando key e message incorretos:
    try:
        encrypt_message(231, 'Hey')
    except TypeError as ex:
        assert type(ex).__name__ == 'TypeError'

    # Testando que key não é um índice válido de message:
    assert encrypt_message(6, 'Hey') == 'yeH'
    assert encrypt_message(12, 'Hey') == 'yeH'

    # Testando se key é ímpar:
    assert encrypt_message(1, 'Hey') == 'H_ey'
    assert encrypt_message(3, 'Friend') == 'dne_irF'

    # Testando se key é par:
    assert encrypt_message(2, 'Hey') == 'He_y'
    assert encrypt_message(4, 'Friend') == 'dn_eirF'

    print('Testes realizados com sucesso')
