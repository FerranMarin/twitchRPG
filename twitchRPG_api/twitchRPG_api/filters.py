from flask import request
import re

int_pattern = re.compile("^[0-9]{1,}$")
datetime_pattern = re.compile(
    "^[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-2][0-9]:[0-5][0-9]:[0-5][0-9]$"
)
date_pattern = re.compile("^\d{4}-\d{2}-\d{2}$")
ip_pattern = re.compile("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$")


def is_numeric_dashed(target):
    return re.compile('^[0-9\-]{1,}$').match(target)


def is_string_dashed(target):
    return re.compile('^[0-9\-A-Z]{1,}$').match(target)


def get_remote_ip():
    proxy_forward = request.headers.getlist("X-Forwarded-For")
    if len(proxy_forward) > 0:
        ip = proxy_forward[0].rpartition(' ')[-1]
        if ip_pattern.match(ip):
            return ip
    return request.remote_addr


def update_channel_status():
    response = {
        'data': {},
        'status': True,
        'errors': []
    }
    required_fields = [
        'territory_id',
        'channels_id'
    ]
    if all(name in required_fields for name in request.json):
        if int_pattern.match(request.json['territory_id']):
            response['data']['territory_id'] = request.json['territory_id']
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for territory_id, must be integer'
            )
        if isinstance(request.json['channels_id'], list):
            response['data']['channels_id'] = [
                a for a in request.json['channels_id'] if int_pattern.match(a)
            ]
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for channels_id, must be integer list'
            )
        response['data']['ip'] = get_remote_ip()
    else:
        response['status'] = False
        response['errors'].append(
            'Missing required fields, check: ' + str(required_fields)
        )
    return response


def update_channel_epg():
    response = {
        'data': [],
        'status': True,
        'errors': []
    }
    json_data = request.get_json()
    for key in json_data:
        for item in json_data[key]:
            if type(item) is list and len(item) == 3:
                if (
                    type(item[0]) is str
                    and datetime_pattern.match(item[1])
                    and datetime_pattern.match(item[2])
                ):
                    item_dict = {
                        "channel": key,
                        "start": item[1],
                        "stop": item[2],
                        "title": item[0]
                    }
                    response['data'].append(item_dict)
                else:
                    response['status'] = False
                    response['errors'].append(
                        'Wrong format for item in list, %s'
                    ) % item
            else:
                response['status'] = False
                response['errors'].append(
                    'Wrong format  or lenght for item list, %s'
                ) % item
    return response


def chromaprint_search():
    response = {
        'data': {},
        'status': True,
        'errors': []
    }
    required_fields = [
        'raw',
        'channel_id',
        'start_timestamp',
        'local_timestamp'
    ]
    if all(name in required_fields for name in request.json):
        if type(request.json['channel_id']) is int:
            response['data']['channel_id'] = request.json['channel_id']
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for channel_id, must be integer'
            )

        start_timestamp = request.json['start_timestamp']
        if datetime_pattern.match(start_timestamp):
            response['data']['start_timestamp'] = start_timestamp
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for start_timestamp, must be datetime'
            )

        local_timestamp = request.json['local_timestamp']
        if datetime_pattern.match(local_timestamp):
            response['data']['local_timestamp'] = local_timestamp
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for local_timestamp, must be datetime'
            )

        if isinstance(request.json['raw'], list):
            response['data']['raw'] = [
                a for a in request.json['raw'] if isinstance(a, int)
            ]
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for raw, must be integer list'
            )
    else:
        response['status'] = False
        response['errors'].append(
            'Missing required fields, check: ' + str(required_fields)
        )
    return response


def adzone_update():
    response = {
        'data': {},
        'status': True,
        'errors': []
    }
    required_fields = [
        'adzone',
        'channel_id',
        'timestamp',
        'local_timestamp'
    ]
    if all(name in required_fields for name in request.json):
        if type(request.json['channel_id']) is int:
            response['data']['channel_id'] = request.json['channel_id']
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for channel_id, must be integer'
            )

        if type(request.json['adzone']) is int:
            response['data']['adzone'] = request.json['adzone']
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for adzone, must be integer'
            )

        timestamp = request.json['timestamp']
        if datetime_pattern.match(timestamp):
            response['data']['timestamp'] = timestamp
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for timestamp, must be datetime'
            )

        local_timestamp = request.json['local_timestamp']
        if datetime_pattern.match(local_timestamp):
            response['data']['local_timestamp'] = local_timestamp
        else:
            response['status'] = False
            response['errors'].append(
                'Wrong format for local_timestamp, must be datetime'
            )
    else:
        response['status'] = False
        response['errors'].append(
            'Missing required fields, check: ' + str(required_fields)
        )
    return response
