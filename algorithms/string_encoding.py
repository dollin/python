import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(threadName)s] %(funcName)s:%(lineno)d %(message)s',
)

def encode(input_str):
    encoded = ''
    curr = ''
    count = 0
    for char in input_str:
        if curr == char:
            count += 1
        else:
            if count > 0:
                encoded += str(count) + curr
            count = 1
            curr = char
    if count > 0:
        encoded += str(count) + curr
    return encoded


def decode(input_str):
    decoded = ''
    count = 0
    for char in input_str:
        if '0' <= char <= '9':
            count = (count * 10) + int(char)
        else:
            decoded += char * count
            count = 0
    return decoded

s = 'aaaaaaaaaabbbccdaa'
logging.info(encode(s))
logging.info(decode(encode(s)))
