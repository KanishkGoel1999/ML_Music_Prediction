import sys

def error_message_detail(error, error_detail:sys):
, ,exc_tb = error_detail.exc_info()
file_name = exc_tb.tb_frame.f_code.co_filename
error_message="Error occured in pytho script name {} line {} error message".format(file_name, exc_tb.tb_lineno,str(error))
