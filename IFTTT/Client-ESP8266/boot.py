# This file is executed on every boot (including wake-boot from deepsleep)

import esp

import gc

import webrepl

webrepl.start()

esp.osdebug(None)

gc.collect()