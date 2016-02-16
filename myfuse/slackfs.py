#!/usr/bin/python
import sys
from fuse import FUSE, Operations
class Slack(Operations):
	"""A simple slackfs that implements mostly readonly options"""
	def __init__(self, arg):
		super(Slack, self).__init__()
		self.arg = arg
		
def main(args):
	pass
if __name__ == '__main__':
	main(sys.argv)