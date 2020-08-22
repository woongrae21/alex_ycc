#Mutations
def mutate_string(string, position, character):
    A = list(string)
    A[position] = character
    string = "".join(A)
    return string
