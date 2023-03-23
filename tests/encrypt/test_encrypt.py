from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError) as error:
        encrypt_message("arroz doce", "é gostoso")

    assert str(error.value) == "tipo inválido para key"

    with pytest.raises(TypeError) as error:
        encrypt_message(2, 1)

    assert str(error.value) == "tipo inválido para message"

    result_key = encrypt_message("arroz doce", 30)
    assert result_key == "ecod zorra"

    result_key = encrypt_message("arroz doce", 4)
    assert result_key == "ecod z_orra"

    result_key = encrypt_message("arroz doce", 4)
    assert result_key != "rra_ecod zo"
