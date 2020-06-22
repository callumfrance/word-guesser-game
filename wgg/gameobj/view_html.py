from .view_abstract import ViewAbstract


class ViewHTML(ViewAbstract):


    def __init__(self):
        self._end = '</div>'
        self._row_st = '<div class="board row">'
        self._vert = '<div class="board edge vert">|</div>'
        self._hori = '<div class="board edge hori">-</div>'
        self._corn = '<div class="board edge corn">+</div>'
        self._alpha_st = '<div class="board alpha">'

    def v_board(self, in_b_str):
        """Method used to print the scrambled 9 letter word
        """
        out_b_str = ""
        for n, i in enumerate(in_b_str):
            if (n % 3 == 0):
                out_b_str += self._end + self._row_st + self._vert
            out_b_str += self._alpha_st + i + "</div>"
            if (n % 3 == 2):
                out_b_str += self._vert
            
        out_b_str = self.v_line_thing() + out_b_str + self.v_line_thing()
        return(out_b_str)

    def v_line_thing(self):
        """Mini method used to print part of the print_board
        """
        x = self._end + self._row_st + self._corn
        x += (self._hori * 3) + self._corn + '</div>'
        return(x)

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
        x = self._row_st
        x += str(in_stats.board_cnt)
        x += str(in_stats.correct)
        x += str(in_stats.incorrect)
        x += str(in_stats.failures)
        x += self._end
        return(x)
