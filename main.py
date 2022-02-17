change_list = (100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05)
for index, inc in enumerate(change_list):
    if total >= inc:
        final_denomination[index] = final_denomination[index] + 1
        total -= inc


    def loshumagic(magic_square):

        """
        Returns True or False if list is a loshu mahic square
        :param magic_square: 2D-grid list
        :precondition: list is only positive integers
        :postcondition: Returns True or False based on magic square
        :return: True if the list is a loshu magic square, False if not

        Test 1: A valid loshu magic, returns true
        Test 2: Invalid loshu magic, returns false

        >>> loshumagic([[6, 1, 8], [7, 5, 3], [2, 9, 4]])
        True
        >>> loshumagic([[4, 9, 1], [3, 2, 7], [3, 0, 6]])
        False
        """
        length = len(magic_square)
        magic_number = 0

        for i in range(0, length):
            prev_number = magic_number
            magic_number = 0
            for j in range(0, length):
                magic_number = magic_number + magic_square[i][j]
            if i == 0:
                prev_number = magic_number

            if prev_number != magic_number:
                return False

        for i in range(0, length):
            prev_number = magic_number
            magic_number = 0
            for j in range(0, length):
                magic_number = magic_number + magic_square[j][i]
            if i == 0:
                prev_number = magic_number

            if prev_number != magic_number:
                return False

        prev_number = magic_number
        magic_number = 0
        for i in range(length):
            magic_number += magic_square[i][i]

        if prev_number != magic_number:
            return False

        prev_number = magic_number
        magic_number = 0
        for i in range(length):
            magic_number += magic_square[i][(length - 1 - i)]

        if prev_number != magic_number:
            return False

        return True


    def main():

        return loshumagic([[4, 9, 2], [3, 5, 7], [8, 1, 6]])


    if __name__ == "__main__":
        main()
