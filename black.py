from board import Board

b = Board()

class Black:
	def __init__(self):
		self.pawn1Pos = b.A7
		self.pawn2Pos = b.B7
		self.pawn3Pos = b.C7
		self.pawn4Pos = b.D7
		self.pawn5Pos = b.E7
		self.pawn6Pos = b.F7
		self.pawn7Pos = b.G7
		self.pawn8Pos = b.H7

	def move(self, selectPawn: str, byWhat: int):
		if selectPawn == "first":
			chosenPawn = self.pawn1Pos
		elif selectPawn == "second":
			chosenPawn = self.pawn2Pos
		elif selectPawn == "third":
			chosenPawn = self.pawn3Pos
		elif selectPawn == "fourth":
			chosenPawn = self.pawn4Pos
		elif selectPawn == "fifth":
			chosenPawn = self.pawn5Pos
		elif selectPawn == "sixth":
			chosenPawn = self.pawn6Pos
		elif selectPawn == "seventh":
			chosenPawn = self.pawn7Pos
		elif selectPawn == "eighth":
			chosenPawn = self.pawn8Pos
		else:
			return "Invalid pawn."
		realPos = chosenPawn + byWhat
		return realPos

# Test
black = Black()
print("Pawn's current square is " + str(black.move("first", 2)) + ".")