non_terminals = ["S", "N", "D", "P",
				"V", "A"]
terminals = ["a","b", "c", "d",
			"e", "f",
			"g", "h","i"]

# Rules of the grammar
R = {
	"S": [["D", "N"]],
	"N": [["P", "N"], ["b"],
			["c"], ["d"]],
	"P": [["V", "A"], ["f"],
			["c"], ["e"]],
	"D": [["a"]],
	"V": [["g"], ["i"]],
	"A": [["f"], ["c"], ["e"],
		["h"]]
	}

def cykParse(inp):
	n = len(inp)
	T = [[set([]) for j in range(n)] for i in range(n)]

	for j in range(0, n):
		for lhs, rule in R.items():
			for rhs in rule:
				if len(rhs) == 1 and rhs[0] == inp[j]:
					T[j][j].add(lhs)

		for i in range(j, -1, -1):
			for k in range(i, j + 1):	
				for lhs, rule in R.items():
					for rhs in rule:
						if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
							T[i][j].add(lhs)

	if len(T[0][n-1]) != 0:
		print("True")
	else:
		print("False")

inp = "a g f c b".split()
cykParse(inp)
