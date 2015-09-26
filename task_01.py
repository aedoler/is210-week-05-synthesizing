#!user/bin/env python
# -*- coding: utf-8 -*-
"Shows date and time"

import datetime

CURDATE = None


def get_current_date():
    """returns date and time of current day

    Variables: none

    Returns: Current date and time if run on command line, else "None"

    Examples:
    import task_01
    task_01.CURDATE
    >>>

    import task_01
    CURDATE
    >>> (2015, 9, 26)

    If run on command line
    task_01.py
    2015-09-26
    """
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
