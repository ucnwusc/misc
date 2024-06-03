import sys
import os

package_path = '/path/to/your/packages'

if package_path not in sys.path:
    sys.path.append(package_path)

import numpy
import pandas
import matplotlib

print("Packages are ready to use.")
