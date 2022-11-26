def test_assert_add():
    assert 3 + 1


def get_text_element(locator):
    return wd.find_element(locator).text
