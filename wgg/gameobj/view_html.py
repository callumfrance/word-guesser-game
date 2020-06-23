from .view_abstract import ViewAbstract
from json import loads


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
        return("Answer was " + ans_str)

    def v_print(self, in_string):
        """Generic view print statement
        """
        return(in_string)


    def v_stats(self, in_stats_js_str):
        """Prints all the stats for the current user's run
        """
        in_stats = loads(in_stats_js_str)

        x = '''
            <div class="row py-4">
                <div class="col-1"></div>
                <div class="col-8">
                    <ul class="list-group">'''
        x += '          <li class="list-group-item list-group-item-success">'
        x += "Correct " + str(in_stats["correct"])
        x += '          </li>'
        x += '          <li class="list-group-item list-group-item-warning">'
        x += "Incorrect " + str(in_stats["incorrect"])
        x += '          </li>'
        x += '          <li class="list-group-item list-group-item-danger">'
        x += "Skipped " + str(in_stats["failures"])
        x += '          </li>'

        x += '          <li class="list-group-item">'
        x += "Correct Words "
        if in_stats["correct_words"]:
            x += '<ul class="list-group">'
            for y in in_stats["correct_words"]:
                x += '<li class="list-group-item py-2 text-success border-success">' + y + '</li>'
            x += '</ul>'
        x += '          </li>'

        x += '          <li class="list-group-item">'
        x += "Skipped Words "
        if in_stats["failure_words"]:
            x += '<ul class="list-group py-2">'
            for y in in_stats["failure_words"]:
                x += '<li class="list-group-item py-2 text-info border-info">' + y + '</li>'
            x += '</ul>'
        x += '          </li>'

        x += '''    </ul>
                </div>
                <div class="col-3"></div>
            </div>
            '''

        return(x)
