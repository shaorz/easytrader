# coding:utf-8
import json
from typing import Mapping


def parse_cookies_str( cookies: str ):
    """
    parse cookies str to dict
    :param cookies: cookies str
    :type cookies: str
    :return: cookie dict
    :rtype: dict
    """
    cookie_dict: Mapping = {}
    for record in cookies.split( ";" ):
        key, value = record.strip().split( "=", 1 )
        cookie_dict[ key ] = value
    return cookie_dict


def file2dict( path: str ) -> json:
    with open( path, encoding="utf-8" ) as f:
        return json.load( f )


def grep_comma( num_str: str ) -> str:
    return num_str.replace( ",", "" )


def str2num( num_str: str , convert_type: str = "float" ):
    num = float( grep_comma( num_str ) )
    return num if convert_type == "float" else int( num )
