#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File         : script.py
# @Date         : 28-12-2021
# @Author       : Payne
# @Email        : wuzhipeng1289690157@gmail.com
# @Desc:    Intercept entry
import pprint
from typing import Any
from config import ResourceList
from process import all_entrances
import json
from urllib.parse import unquote
from mitmproxy import ctx


# def request(flow):
#     ctx.log.info(str(flow.request.url))
#     ctx.log.info(str(flow.request.method))
#     ctx.log.info(str(flow.request.path))


def response(flow) -> None:
    """
    :param flow:
    :return:
    """
    for source in ResourceList.keys():
        if ResourceList.get(source) in flow.request.url:
            body = unquote(flow.response.text)
            data = json.loads(body)
            results: list[Any] | Any = data['data']['items'] or []
            ctx.log.info(f"First UserId: {results[0]['note']['id']} Processing...: ")
            all_entrances(source, results)
