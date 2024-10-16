import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

img = os.path.join(base_dir, 'assets','images','violence.png')
print(img)



