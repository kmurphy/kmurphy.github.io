import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from IPython import utils
from IPython.display import display, HTML, Markdown

import os

# load libraries
import numpy as np
import scipy as sci
import sympy as sym
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

__version__ = 2020.0
    
def setup_practical(notebook_state):
    
    missing_your_student_number = int('your_student_number' not in notebook_state or notebook_state['your_student_number']=='')
    missing_your_name = int('your_name' not in notebook_state or notebook_state['your_name']=='')
    messages = ['',  'name in the cell', 'student number in the cell', 'student number and name in the cells']
    if missing_your_student_number+missing_your_name>0:
        message = messages[2*missing_your_student_number+missing_your_name]
        html = f'<h2>Warning: Please enter your {message} above and click on the arrow on top-left or Shift+Enter to save data.</h2>'
        return HTML(html)

    html = 'Python practical setup tools (version %s). See <a target="_blank" href="https://moodle.wit.ie/course/view.php?id=168360&section=3">python practicals section on Moodle for details.</a>' % __version__
    return HTML(html)

from .logic import *