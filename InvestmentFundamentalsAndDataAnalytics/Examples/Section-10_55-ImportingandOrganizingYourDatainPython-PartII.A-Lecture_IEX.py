#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import numpy as np
import pandas as pd
# In[ ]:
ser = pd.Series(np.random.random(5), name = "Column 01")
# In[ ]:
ser
# In[ ]:
ser[2]
