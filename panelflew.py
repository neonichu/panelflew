#!/usr/bin/env python

from cbz import CBZ

import os.path
import xml.etree.ElementTree as ET

class PanelFlyIssue:
	def __init__(self, xml_path):
		path = os.path.dirname(xml_path)
		doc = ET.parse(xml_path)
		issue = doc.getroot()
		self.name = issue.find('publication').text + ' ' + issue.find('name').text

		self.pages = []
		for pageNode in issue.find('pages').iter('page'):
			try:
				pageNum = int(pageNode.get('number', 0))
			except:
				pageNum = self.pages[-1]['number'] + 1

			page = { 	'path': os.path.join(path, pageNode.get('path')), 
						'number': pageNum }

			self.pages.append(page)

	def __str__(self):
		return self.name

def panelfly_export(filename):
	issue = PanelFlyIssue(filename)
	print 'Exporting %s...' % issue.name
	cbz = CBZ([page['path'] for page in issue.pages])
	cbz.export(issue.name + '.cbz')

def panelfly_visitor(arg, dirname, files):
	for filename in files:
		if filename == 'page_index.xml':
			panelfly_export(os.path.join(dirname, filename))

if __name__ == '__main__':
	path = os.path.expanduser('~/Desktop/Panelfly/Issues')
	os.path.walk(path, panelfly_visitor, None)
