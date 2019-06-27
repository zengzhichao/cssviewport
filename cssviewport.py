import sublime
import sublime_plugin
import re
import time
import os

SETTINGS = {}

#plugin_loaded() will be called when the API is ready to use. 
def plugin_loaded():
	init_settings()

def init_settings():
    get_settings()
    sublime.load_settings('cssviewport.sublime-settings').add_on_change('get_settings', get_settings)

def get_settings():
    settings = sublime.load_settings('cssviewport.sublime-settings')
    SETTINGS['disable'] = settings.get('disable', 0)
    SETTINGS['unitToCovert'] = settings.get('unitToCovert', 'px')
    SETTINGS['unitPrecision'] = settings.get('unitPrecision', 5)
    SETTINGS['viewportWidth'] = settings.get('viewportWidth', 320)
    SETTINGS['viewportUnit'] = settings.get('viewportUnit','vw')
    SETTINGS['available_file_types'] = settings.get('available_file_types', ['.css', '.less', '.sass'])

def get_setting(view, key):
	return view.settings().get(key, SETTINGS[key])

def px_replace(value ,viewportUnit, viewportWidth, unitPrecision):
	return round(float(value) / viewportWidth * 100, unitPrecision)


class cssviewportCommand(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		# print('test1 start {0}, {1}'.format(prefix, locations))

		#disable this plugin
		if(get_setting(view, 'disable')):
			return []

		# only works on specific file types
		fileName, fileExtension = os.path.splitext(view.file_name())
		if not fileExtension.lower() in get_setting(view, 'available_file_types'):
			return []
		
		location = locations[0]
		snippets = []

		# get vw match
		match = re.compile("([\d.]+)p(x)?").search(prefix)
		if match:
			lineLocation = view.line(location)
			line = view.substr(sublime.Region(lineLocation.a, location))
			value = match.group(1)

			viewportUnit = get_setting(view , 'viewportUnit')
			viewportWidth = get_setting(view, 'viewportWidth')
			unitPrecision = get_setting(view, 'unitPrecision')
			vwValue = px_replace(value, viewportUnit, viewportWidth, unitPrecision)

			# set completion snippet
			snippets += [(value + 'px ->' + viewportUnit + '(' + str(viewportWidth) + ')', str(vwValue) + viewportUnit)]
		return snippets

