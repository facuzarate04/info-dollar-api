from dataclasses import replace
from scrap import DollarBlueScrap 
from scrap import DollarOficialScrap 
import helpers
import os
from notify import Notify
import json


def dollar_blue():
    title = DollarBlueScrap.get_data()['title']
    date = DollarBlueScrap.get_data()['date']
    buy = helpers.parse_to_float(DollarBlueScrap.get_data()['values']['buy'])
    sell = helpers.parse_to_float(DollarBlueScrap.get_data()['values']['sell'])
    variation = helpers.parse_to_float(DollarBlueScrap.get_data()['variation'])

    variation_notify_diff = float(os.getenv('VARIATION_BLUE_NOTIFY_DIFF'))

    response = {
        'title': title,
        'date': date,
        'buy': buy,
        'sell': sell,
        'variation': variation 
    }

    if variation >= variation_notify_diff or variation <= -variation_notify_diff:
        Notify.send_mail_notification()

    return response


def dollar_oficial():
    title = DollarOficialScrap.get_data()['title']
    date = DollarOficialScrap.get_data()['date']
    buy = helpers.parse_to_float(DollarOficialScrap.get_data()['values']['buy'])
    sell = helpers.parse_to_float(DollarOficialScrap.get_data()['values']['sell'])
    w_tax = helpers.parse_to_float(DollarOficialScrap.get_data()['values']['w_tax'])
    w_full_tax = helpers.parse_to_float(DollarOficialScrap.get_data()['values']['w_full_tax'])
    variation = helpers.parse_to_float(DollarOficialScrap.get_data()['variation'])

    variation_notify_diff = float(os.getenv('VARIATION_OFICIAL_NOTIFY_DIFF'))

    response = {
        'title': title,
        'date': date,
        'buy': buy,
        'sell': sell,
        'w_tax': w_tax,
        'w_full_tax': w_full_tax,
        'variation': variation 
    }

    if variation >= variation_notify_diff or variation <= -variation_notify_diff:
        Notify.send_mail_notification()

    return response