from __future__ import print_function

import os
from nude import Nude

ROOT = os.path.dirname(os.path.abspath(__file__))


# n = Nude(os.path.join(ROOT, '../../public/images/1463988870263AE1CF23.jpg'))
# n.parse()
# nude = 1 if n.result else 0
# print(nude)
# print(n.result, n.inspect())

n = Nude(os.path.join(ROOT, '../../public/images/1463989011986ACBE628.jpg'))
n.parse()
print(n.result, n.inspect())


# n = Nude(os.path.join(ROOT, '../../public/images/test8.jpg'))
# n.parse()
# print(n.result, n.inspect())
#
#
#
#
# n = Nude(os.path.join(ROOT, '../../public/images/test7.jpg'))
# n.parse()
# print(n.result, n.inspect())
#
#
#
# n = Nude(os.path.join(ROOT, '../../public/images/damita.jpg'))
# n.parse()
# print(n.result, n.inspect())
#
# n = Nude(os.path.join(ROOT, '../../public/images/damita2.jpg'))
# n.parse()
# print(n.result, n.inspect())
#
# n = Nude(os.path.join(ROOT, '../../public/images/test6.jpg'))
# n.parse()
# print(n.result, n.inspect())
#
# n = Nude(os.path.join(ROOT, '../../public/images/test2.jpg'))
# n.parse()
# print(n.result, n.inspect())
