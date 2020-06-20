from abc import ABC, abstractmethod


class ViewAbstract(ABC):


    @abstractmethod
    def v_board(self, board_str):
        """Method used to print the scrambled 9 letter word
        """
        pass

    @staticmethod
    @abstractmethod
    def v_line_thing():
        """Mini method used to print part of the print_board
        """
        pass

    @staticmethod
    @abstractmethod
    def v_user_in():
        """Method used to display a user's current guess
        """
        pass

    @abstractmethod
    def v_result(self, ans_str):
        """Method used to output the result of a user's guess
        """
        pass

    @abstractmethod
    def v_print(self, in_string):
        """Generic view print statement
        """
        pass

    @abstractmethod
    def v_stats(self, in_stats):
        """Prints all the stats for the current user's run
        """
        pass
