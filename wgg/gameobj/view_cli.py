from view_abstract import ViewAbstract


class ViewCLI(ViewAbstract):


    def v_board(self, in_b_str):
        """Method used to print the scrambled 9 letter word
        """
        out_b_str = ""
        for n, i in enumerate(in_b_str):
            if (n % 3 == 0):
                out_b_str += "\n| "
            out_b_str += i + " "
            if (n % 3 == 2):
                out_b_str += "|"
            
        out_b_str = self.v_line_thing() + out_b_str + self.v_line_thing()
        print(out_b_str)

    @staticmethod
    def v_line_thing():
        """Mini method used to print part of the print_board
        """
        return("\n+-------+")

    def v_user_in(self):
        """Method used to display a user's current guess
        """
        return(input("\n> ").strip())

    def v_result(self, ans_str):
        """Method used to output the result of a user's guess
        """
        print("Answer was " + ans_str)

    def v_print(self, in_string):
        """Generic view print statement
        """
        print(in_string)


    def v_stats(self, in_stats):
        """Prints all the stats for the current user's run
        """
        print(in_stats)
