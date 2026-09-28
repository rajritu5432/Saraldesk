from saraldesk.privacy_shield import mask_pii, verhoeff_valid

VALID = "234567890009"   # checksum-valid test number
INVALID = "234567890000"   # fails the checksum


def test_valid_aadhaar_is_masked():
    text, found = mask_pii("Aadhaar " + VALID)
    assert "aadhaar" in found and VALID[-4:] in text and VALID[:4] not in text


def test_invalid_12_digit_number_is_not_treated_as_aadhaar():
    assert not verhoeff_valid(INVALID)
    _, found = mask_pii("Ref " + INVALID)
    assert "aadhaar" not in found


def test_pan_and_phone_masked():
    text, found = mask_pii("PAN ABCDE1234F call 9876543210")
    assert "pan" in found and "phone" in found
    assert "ABCDE" not in text and "98765" not in text
