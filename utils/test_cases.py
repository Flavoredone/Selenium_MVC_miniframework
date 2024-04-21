#!/usr/bin/env python
# -*- coding: utf8 -*-

import json


def test_cases(number):
    return list(set_test_cases())[number]


def set_test_cases():
    with open('../utils/test_data.json', 'r') as file:
        cases = json.load(file).values()
    return cases


def generate_test_cases():
    """function that generates test data json file"""
    with open('../utils/test_data.json', 'a') as f:
        f.write(json.dumps({
            "case number": "description",
            "1": "Test Case #1. Help form. All features worked out (Help response is displayed)",
            "2": "Test Case #2. Timer. All features worked out (The timer starts from zero)",
            "3": "Test Case #3. Valid password. All features worked out (The second card is open)",
            "4": "Test Case #4. Invalid password. All features worked out (The second card isn't open)",
            "5": "Test Case #5. Extensions. All features worked out (More functionality was added)",
        }, ensure_ascii=False, indent=3))
