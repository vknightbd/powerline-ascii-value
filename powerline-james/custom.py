# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

try:
	import vim
except ImportError:
	vim = object()

from powerline.theme import requires_segment_info

@requires_segment_info
def ascii_value(pl, segment_info):
	'''Show ascii value under cursor.
	'''
	#if segment_info['mode'] in ['i', 'ic', 'ix']:
	if segment_info['mode'] != 'n':
		return None

	line, col  = segment_info['window'].cursor
	buf = segment_info['buffer']

  # skip if line empty
	if len(buf[line - 1]) == 0:
	  return None

	contents = ord(buf[line - 1][col])

	return [{
		'contents': ' [%s] ' % contents,
		'highlight_groups': ['system_load', 'background']
#		'highlight_groups': ['user', 'superuser', 'background']
	}]
