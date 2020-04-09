def get_payloads():
    file = open('static/files/payloads.txt', 'r')
    return [payload.strip('\n') for payload in file.readlines()]


def get_encoders():
    file = open('static/files/encoders.txt', 'r')
    return [encoder.strip('\n') for encoder in file.readlines()]


def get_formats():
    file = open('static/files/formats.txt', 'r')
    return [payload_format.strip('\n') for payload_format in file.readlines()]


def set_cmd(payload, encoder, variable_name, payload_format, bad_chars, arch):
    cmd = f"msfvenom -p {payload} -e {encoder} -v {variable_name} -f {payload_format} " \
          f"-b {bad_chars} -a {arch}"
    """
    
    NOT IMPLEMENTED YET
    
    """