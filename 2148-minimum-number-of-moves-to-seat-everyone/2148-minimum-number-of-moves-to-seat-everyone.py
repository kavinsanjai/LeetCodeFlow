class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        new=0
        for i in range(0,len(seats)):
            new+=abs(seats[i]-students[i])
        return new
        