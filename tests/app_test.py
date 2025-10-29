from streamlit.testing.v1 import AppTest

def test_critique_single():
    """A user enters some text to be critiqued and gets a response"""
    at = AppTest.from_file("critic.py",default_timeout=10).run()

    assert at.chat_message[0].markdown[0].value == "How can I help you?"
    assert at.chat_message[0].avatar == "assistant"

    at.chat_input[0].set_value("Please critique my short story: For sale: Baby shoes, never worn.").run()

    assert at.chat_message[1].markdown[0].value == "Please critique my short story: For sale: Baby shoes, never worn."
    assert at.chat_message[1].avatar == "user"

    # Model should identify obvious widely known story
    assert "Ernest Hemingway" in at.chat_message[2].markdown[0].value
    assert at.chat_message[2].avatar == "assistant"