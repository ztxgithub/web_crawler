#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
line = "你"
regex_str = "([\u4E00-\u9FA5])"
match_obj = re.match(regex_str,line)
if match_obj:
    print(match_obj.group(1))