#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "15921659"))
    API_HASH = os.environ.get("API_HASH", "3dc791023550d5011f7ac0e2c1fd46f6")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5581535747:AAECKAlzKaPA6JVj8FM-FMJql40I0KBkeRI") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", "1958320314")
    SESSION = os.environ.get("AQCgzGd2ORuCuoDnHv3TGNDSMEO-HHbcitIatHRRXDRaDxBdodBgU96IO_6HtX092WTdFuQVx-_z2psJRe9kSP9FNt0hyoZZZKrzn6OF1icZOUazSIN5KEfTcj6ioYv4a2A6gTgJeOT3Yzlrt20APvfp91QUlFwwPP7VWYAoNYU7JW1AQVNUeGHqnj-0mvVadJWgkWPl2Sgslf_sR9wefyVA2qqO_mbdIG4k0F4mzDynmTRwMWlEd03kgYvpo3lsE1b_R4Qim6v_nzKyyGyYL7Sy9BIv7_NB8GMoRXNfyqyXoqGAWUki7aU6EcupDmN3m5zFFeFt88tj9X2vvsEUbBOadLmYugA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
