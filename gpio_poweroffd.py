#!/usr/bin/env python2

import logging
import logging.handlers
import RPi.GPIO as GPIO
import subprocess
import time


console_format = '%(name)-13s %(levelname)-8s %(message)s'
syslog_format = 'thinkpad-scripts: %(name)s %(levelname)s %(message)s'


def setup_GPIO(channel):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(channel, GPIO.IN)


def setup_logging():
    logging.basicConfig(level=logging.INFO, format=console_format)

    syslog = logging.handlers.SysLogHandler(address='/dev/log')
    syslog.setLevel(logging.DEBUG)
    syslog.setFormatter(logging.Formatter(syslog_format))
    logging.getLogger().addHandler(syslog)

    return logging.getLogger(__name__)


def main(channel):
    setup_GPIO(channel)
    logger = setup_logging()
    while True:
        GPIO.wait_for_edge(channel, GPIO.FALLING)
        press = time.time()
        while (time.time() - press) < 5:
            time.sleep(0.05)
            if GPIO.input(channel):
                break
        else:
            logger.info('Calling poweroff.')
            subprocess.Popen(['poweroff'])


if __name__ == '__main__':
    main(3)
