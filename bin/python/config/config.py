# config.py
'''
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001402319155292f806e5a1ba5342d2a497c63314b1c77f000
'''
import config_dev

configs = config_dev.configs
def merge(d1,d2):
	return dict(d1.items() + d2.items())

try:
    import config_prod
    configs = merge(configs, config_prod.configs)
except ImportError:
    pass