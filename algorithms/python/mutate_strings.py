# GOAL: Transform string A into string B, character by character.
# Only display/store the word if a modification occurs at index i.

def mutate_my_strings(s1, s2):
    res = [s1]
    current = list(s1)
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            current[i] = s2[i]
            res.append("".join(current))
            
    return "\n".join(res)

if __name__ == "__main__":
    resultat = mutate_my_strings('bubble gum', 'turtle ham')
    print(resultat)
