import sys
import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() ## we are not interested in first two things third thing is all error details
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in pythone script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message #When we print thwe custom exception it is going to print the error message
    

    