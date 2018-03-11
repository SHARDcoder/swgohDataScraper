"""
MIT License

Copyright (c) 2018 SHARDcoder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests

class characters():
	def __init__(self):
		pass
	
	def __main__(self):
		pass
	
	def convertNameFormat(self, name):
		name = name.lower()
		name = name.replace(' ', '-')
		name = name.replace('"', '')
		return name
	
	def get_overview(self, name):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		overviewStart = scrapedLines.index('<ul class="panel-menu">')
		scrapedLines = scrapedLines[overviewStart + 1:overviewStart + 12]
		
		scrapedLines[2] = scrapedLines[2].replace('<h5 class="m-y-0">', '')
		scrapedLines[2] = scrapedLines[2].replace('</h5>', '')
		scrapedLines[6] = scrapedLines[6].replace('<h5 class="m-y-0">', '')
		scrapedLines[6] = scrapedLines[6].replace('</h5>', '')
		scrapedLines[10] = scrapedLines[10].replace('<h5 class="m-y-0">', '')
		scrapedLines[10] = scrapedLines[10].replace('</h5>', '')
		
		del scrapedLines[8]
		del scrapedLines[7]
		del scrapedLines[4]
		del scrapedLines[3]
		del scrapedLines[0]
		
		return scrapedLines
	
	def get_power(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Power</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
	
	def get_strength_growth_modifier(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<td>Strength Growth Modifier</td>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_agility_growth_modifier(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Agility Growth Modifier</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_intelligence_growth_modifier(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Intelligence Growth Modifier</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_strength(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Strength</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_agility(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Agility</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_intelligence(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Intelligence</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_speed(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Speed</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_health(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Health</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_physical_damage(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Physical Damage</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_special_damage(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Special Damage</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
		
	def get_special_critical_rating(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Special Critical Rating</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_armor(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Armor</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_resistance(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Resistance</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def getphysical_critical_rating(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Physical Critical Rating</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_armor_penetration(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Armor Penetration</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_resistance_penetration(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Resistance Penetration</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_potency(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Potency</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_health_steal(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Health Steal</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_tenacity(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Tenacity</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_dodge_rating(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Dodge Rating</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_deflection_rating(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Deflection Rating</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
	
	def get_protection(self, name, star = 7):
		rawScraped = requests.get('https://swgoh.gg/characters/' + str(self.convertNameFormat(name)) + '/stats/')
		
		scrapedLines = rawScraped.text.splitlines()
		
		dataStart = scrapedLines.index('<th>Protection</th>')
		
		returnData = scrapedLines[dataStart + (8 - star)]
		
		returnData = returnData.replace('<td>', '')
		returnData = returnData.replace('</td>', '')
		
		return returnData
