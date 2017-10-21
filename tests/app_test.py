# -*- coding: utf-8 -*-
import unittest
import os

class test_AndroidExamplesIV():

	def compruebaarchivos(path):
		os.path.exists(path)
		
	def devuelvetrue(): 
    		return 1 
 
	def devuelvefalse():
		return 0

if __name__ == '__main__':
    unittest.main()
