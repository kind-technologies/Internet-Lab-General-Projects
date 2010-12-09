import os

# Dynamically Load All the Controllers
for module in os.listdir(os.path.dirname(__file__) + '/controllers/'):
	if module == '__init__.py' or module[-3:] != '.py':
		continue
	
	mod_name = "controllers." + module[:-3]
	exec("from " + mod_name + " import *")
del module

# Dynamically Load All the Models
for module in os.listdir(os.path.dirname(__file__) + '/models/'):
	if module == '__init__.py' or module[-3:] != '.py':
		continue
	
	mod_name = "models." + module[:-3]
	exec("from " + mod_name + " import *")
del module

