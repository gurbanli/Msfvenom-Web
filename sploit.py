import json
import os


def get_payloads():
    file = open('static/files/payloads.txt', 'r')
    return [payload.strip('\n') for payload in file.readlines()]


def get_encoders():
    file = open('static/files/encoders.txt', 'r')
    return [encoder.strip('\n') for encoder in file.readlines()]


def get_formats():
    file = open('static/files/formats.txt', 'r')
    return [payload_format.strip('\n') for payload_format in file.readlines()]


def get_options(payload_name):
    payload_name = payload_name + '.txt'
    file = open('static/options/' + payload_name, 'r')
    options = {
        'options': [option.strip('\n') for option in file.readlines()]
    }
    return json.dumps(options)


def generate_payload(payload, options, encoder, variable_name, payload_format, bad_chars):
    try:
        option_parameters = ''
        for key, value in options.items():
            option_parameters += key + '=' + value + ' '
        cmd = f"msfvenom -p {payload} {option_parameters} -e {encoder} -v {variable_name} " \
              f"-f {payload_format} -b '{bad_chars}'"
        stream = os.popen(cmd)
        result = stream.read()
        return result
    except Exception:
        return "Internal Server Error"
