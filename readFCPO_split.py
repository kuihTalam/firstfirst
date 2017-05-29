# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:04:41 2017

@author: TSO1PG1
"""

import pandas as pd

full_file_path = r'D:\Python\FCPO.html'
source = open(full_file_path, 'r', encoding='utf8').read()

value = str(source.split('<table id="bm_derivatives_prices_table" summary="Derivatives By Contract Code - FCPO" class="bm_center bm_dataTable">')[1].split('<div class="oi_wrapper" style="position: relative; left: 20px; bottom: 158px;">')[2])
print(value.split()[40])