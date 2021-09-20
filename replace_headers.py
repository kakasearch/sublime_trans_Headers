import sublime, sublime_plugin
import re
class RephCommand(sublime_plugin.TextCommand):
	def handle(self,m):
	   m2 = m.group(2).replace("\n",'')
	   return f'"{m.group(1)}": \'{m2}\','
	def run(self, edit):
		# print(self.view.substr(self.view.sel()[0]))
		sels = self.view.sel()
		for sel in sels:
			if sel.empty():
				self.view.show_popup("请先选择headers文本！！", sublime.HIDE_ON_MOUSE_MOVE_AWAY, -1, 600, 600)
				continue
			str_ = self.view.substr(sel)
			str_ = str_[:-1] if str_[-1]=="\n" else str_
			str_ = re.sub(r"(.*):\s(.*)",self.handle,str_)
			str_ = "headers ={\n\t%s\n}"%('\n\t'.join(str_.split('\n')))
			# print(str_)
			self.view.replace(edit,sel,str_ )

