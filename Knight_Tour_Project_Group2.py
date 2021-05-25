import sys

class KnightsTour:
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.flag = False

        self.board = []
        self.generate_board()

    def path_length (self):
        print ("\nPath length is : ", counter)

    def path_existance (self):
        if exist == True:
            pass
        else:
            print ("\n ====== Path not found ======")

    def generate_board(self):
        """
        Creates a nested list to represent the game board
        """
        for i in range(self.h):
            self.board.append([0]*self.w)

    def print_board(self):
        print ("  ")
        print ("Knight Tour on ", self.h, " X ", self.w, " board :")
        print ("---------------------")
        for elem in self.board:
            print (elem)
        print ("---------------------")
        print ("  ")

    def generate_legal_moves(self, cur_pos):
        """
        Generates a list of legal moves for the knight to take next
        """
        possible_pos = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_offsets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if (new_x >= self.h):
                continue
            elif (new_x < 0):
                continue
            elif (new_y >= self.w):
                continue
            elif (new_y < 0):
                continue
            else:
                possible_pos.append((new_x, new_y))

        return possible_pos

    def sort_lonely_neighbors(self, to_visit):
        """
        It is more efficient to visit the lonely neighbors first, 
        since these are at the edges of the chessboard and cannot 
        be reached easily if done later in the traversal
        """
        neighbor_list = self.generate_legal_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            np_value = self.board[neighbor[0]][neighbor[1]]
            if np_value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.generate_legal_moves(empty)
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key = lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]

        return sorted_neighbours

    def tour(self, n, path, to_visit):
        """
        Recursive definition of knights tour. Inputs are as follows:
        n = current depth of search tree
        path = current path taken
        to_visit = node to visit
        """
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit) #append the newest vertex to the current point
        print ("Visiting: ", to_visit)
        global counter
        counter = counter + 1
        global exist
        exist = False
        repeat = self.w*self.h

        if n == repeat: #if every grid is filled
            self.print_board()
            print ("Path movement in coordinate :")
            print (path)
            print ("---------------------")
            self.path_length()
            print ("\n====== Done! ======")
            exist = True

        else:
            sorted_neighbours = self.sort_lonely_neighbors(to_visit)
            for neighbor in sorted_neighbours:
                if repeat == counter:
                    break
                self.tour(n+1, path, neighbor)
            
            #If we exit this loop, all neighbours failed so we reset
            if sorted_neighbours != 0 and counter != repeat and n!=1:
                self.board[to_visit[0]][to_visit[1]] = 0
                path.pop()
                print ("Going back to : ", path[-1])
    
            elif sorted_neighbours != 0 and counter == repeat and n==1:
                self.path_existance()
            


if __name__ == '__main__':
    #Define the size of grid by inputing value of n
    while True:
        while True:
            n = input("\nPlease enter a positive integer for grid size n x n : ")
            try:
                value = int(n)
                if value > 0 :
                    print("Input is a positive integer :", value,"\n")
                    break;
                else :
                    print("!!! THIS IS NEGATIVE INTEGER !!! : ", value,"\n")
            except ValueError:
                try:
                    float(n)
                    print("!!! THIS IS FLOAT NUMBER !!! ", n, "\n")
                except ValueError:
                    print("!!! THIS IS NOT A NUMBER !!! \n")
        n = value
        counter = 0
        kt = KnightsTour( n, n)
        kt.tour(1, [], (0,0))
        print ("\n===================================")
        print ("\nDo you wish to enter other value for grid size?")
        print ("Please enter :")
        print ("\n Y for Yes \n N for No")

        while True:
            answer = input("\nAnswer : ")
            if answer == 'y' or answer == 'Y' :
                break
            elif answer == 'n' or answer == 'N' :
                sys.exit(1)
            else:
                print (" Please enter valid answer only ")
    
            
    
