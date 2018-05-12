#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
line = "booooobb123"
regex_str = ".*(b.*b).*"
match_obj = re.match(regex_str,line)
if match_obj:
    print(match_obj.group(1))
