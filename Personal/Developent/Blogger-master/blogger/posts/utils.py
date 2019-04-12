import datetime
import re
import math
from django.utils.html import strip_tags

def count_words(html_strings):
	word_string=strip_tags(html_strings)
	matching_words = re.findall(r'\w+', word_string)
	count = len(matching_words)
	return count

def get_read_time(html_strings):
	count = count_words(html_strings)
	read_time_min = (count/200.0)+1
	read_time_sec = read_time_min*60
	read_time = str(datetime.timedelta(minutes=read_time_min))
	return read_time