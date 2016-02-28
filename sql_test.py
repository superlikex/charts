#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# *************************************************************
# Filename @ sql_test.py
# Author @ Likex
# Create date @ 2016-02-27 20:04:46
# Description @ 
# *************************************************************



# Script starts from here

from manage import User
from manage import db
b=User(username='david')
c=User(username='ming')
d=User(username='li')
db.session.add_all([b,c,d])
db.session.commit()
