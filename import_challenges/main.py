
import utils #import another file
#from utils import greeting #this will also work 

#both will work unless if __name__ == '__main__': is used

import people
from people import names

print(names.members) #prints list from names.py


