import base64

# as example
base64_encoded = 'c2hvcElkOjEyMzQuc2NpZDo0MzIxLmN1c3RvbWVyTnVtYmVyOmFiYzAwMC5zaG9wQXJ0aWNsZUlkOjU2Nzg5MC5wYXltZW50VHlwZTpBQy5vcmRlck51bWJlcjphYmMxMTExMTExLmN1c3ROYW1lOkpvaG4gRG9lLmN1c3RBZGRyOtCc0L7RgdC60LLQsCwg0LAv0Y8gMTAwLm9yZGVyRGV0YWlsczrQodGH0LDRgdGC0YzQtSDQtNC70Y8g0LLRgdC10YUsINCyINC/0LDQutC10YLQuNC60LDRhSwg0YDQvtGB0YHRi9C/0YzRjg=='


def decode_base64_to_dict(encoded_string):
    decoded_string = decode_base64_to_string(encoded_string)
    decoded_list = create_list(decoded_string)
    decoded_dict = {
        key: int(value) if value.isnumeric() else value
        for key, value in split_pair_by_key_and_value(decoded_list)
    }
    return decoded_dict


def decode_base64_to_string(encoded_string):
    return base64.b64decode(encoded_string).decode('utf8')


def create_list(decoded_string):
    return decoded_string.split('.')


def split_pair_by_key_and_value(decoded_list):
    for pair in decoded_list:
        yield pair.split(':')


print(decode_base64_to_dict(base64_encoded))

