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
			page = { 	'path': os.path.join(path, pageNode.get('path')), 
						'number': int(pageNode.get('number', 0)) }
			self.pages.append(page)

	def __str__(self):
		return self.name

if __name__ == '__main__':
    issue = PanelFlyIssue('/Users/neonacho/Desktop/Panelfly/Issues/2/1/page_index.xml')
    cbz = CBZ([page['path'] for page in issue.pages])
    cbz.export(issue.name + '.cbz')
