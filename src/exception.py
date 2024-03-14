import os,sys

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys) :
        super().__init__(error_message)
        self.message = CustomException.get_detailed_error_message(error_message,error_detail)


    @staticmethod
    def get_detailed_erro_message(error_message:Exception,error_detail:sys):
        """
        This function returns detailed error message
        """
        _,_,exec_tb = error_detail.exc_info()
        filename = exec_tb.tb_frame.f_code.co_filename
        line_number = exec_tb.tb_lineno
        execpt_line_number = exec_tb.tb_frame.f_lineno
        message = f"""
                Error occurred in Script: {filename},
                \n try block line Number: {line_number} and
                \n exception line Number: {execpt_line_number}
                """
        return message
