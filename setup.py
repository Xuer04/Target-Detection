# -*- coding:utf-8 -*-
"""
Author: Vercent
Date:2022 年 01 月 23 日 
Title:
"""
from cx_Freeze import setup, Executable

setup(name="Simple Object Detection software",
      version="0.1.0",
      description="This software detects objects in realtime",
      executables=[Executable("main.py")]
      )
