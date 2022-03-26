#!/usr/bin/env python
# coding: utf-8

# In[26]:


import itertools
import threading
import time
import sys
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 
class Loading:
    def __init__(self,status = True,text_start = 'loading',text_end = 'Done!'):
        self.status = status
        self.text_start = text_start
        self.text_end = text_end
        self.start_line_len = len(self.text_start)
    def start(self,text_start = 'loading',text_end = 'Done!'):
        self.status = False
        self.text_start = text_start
        self.text_end = text_end
        t = threading.Thread(target=self.animate)
        t.start()
    def stop(self,text_start = 'loading',text_end = 'Done!'):
        self.text_start = text_start
        self.text_end = text_end
        self.status = True
#         self.animate()
    def animate(self):
        for c in itertools.cycle(['.', ' .', '  .', '    ']):
            if self.status:
                break
            sys.stdout.write('\r'+self.text_start+ c)
            sys.stdout.flush()
            time.sleep(0.3)
        sys.stdout.write('\r'+self.text_end)
        for x in range(self.start_line_len):
            sys.stdout.write(CURSOR_UP_ONE) 
            sys.stdout.write(ERASE_LINE)


# In[27]:


# import sys
# CURSOR_UP_ONE = '\x1b[1A' 
# ERASE_LINE = '\x1b[2K' 
# sys.stdout.write('test .')
# sys.stdout.write('new') 


# In[28]:


# import itertools
# import threading
# import time
# import sys
# status = False
# CURSOR_UP_ONE = '\x1b[1A' 
# ERASE_LINE = '\x1b[2K' 
# def animate():
#     for c in itertools.cycle(['.', ' .', '  .', '    ']):
#         if status:
#             break
#         sys.stdout.write('\rloading ' + c)
#         sys.stdout.flush()
#         time.sleep(0.3) 
#     sys.stdout.write('\rDone!')
#     sys.stdout.write(ERASE_LINE)

# t = threading.Thread(target=animate)
# t.start()

# time.sleep(1)
# status = True


# In[30]:





# In[ ]:




