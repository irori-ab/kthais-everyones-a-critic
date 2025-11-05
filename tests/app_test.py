from streamlit.testing.v1 import AppTest


def test_critique_single():
    """A user enters some text to be critiqued and gets a response"""
    at = AppTest.from_file("critic.py", default_timeout=10).run()

    at.radio[0].set_value("encouraging")

    assert (
        at.chat_message[0].markdown[0].value
        == "I will provide feedback on your writing"
    )
    assert at.chat_message[0].avatar.endswith(".png")

    at.chat_input[0].set_value(
        "Please critique my short story: For sale: Baby shoes, never worn."
    ).run()

    assert (
        at.chat_message[1].markdown[0].value
        == "Please critique my short story: For sale: Baby shoes, never worn."
    )
    assert at.chat_message[1].avatar == "user"

    response = str(at.chat_message[2].markdown[0].value)

    assert "tone" in response

    assert at.chat_message[2].avatar.endswith(".png")
