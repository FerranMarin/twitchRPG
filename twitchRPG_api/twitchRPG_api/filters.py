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
