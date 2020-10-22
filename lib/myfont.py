import platform
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 들여오는 library
"""
시스템에 따라 기본 한글 폰트를 읽어 들인다.
"""
pattern = re.compile("Linux|Ubuntu")
    
# 폰트를 적재한다.
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif pattern.search(platform.platform()):
#elif 'Ubuntu' in platform.platform() or 'Linux' in platform.platform():
    path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif 'SuSE' in platform.platform():
    path = "/usr/share/fonts/truetype/NanumGothic.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 