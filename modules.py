import time
import math
import string
import sys
import os
import re
# import cv2 
import threading
import object_detection
import tensorflow as tf
from google.protobuf import text_format
from object_detection.protos import pipeline_pb2
from object_detection.utils import  config_util, label_map_util, visualization_utils as viz_utils
from object_detection.builders import model_builder
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
import glob


import pandas as pd

from io import StringIO
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5 import QtGui, QtCore

from datetime import date
from datetime import datetime as dt
try:
    from ui_addStudentUI import *
    from ui_mainWindowUI import *
    import ui_addStudentUI
    import ui_mainWindowUI
    
except:
    print("somme ui modules not exist")
