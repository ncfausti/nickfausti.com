def ListPermutations(s):
    
    def RecPermute(soFar, rest):
        if rest == "":
            print(soFar)
        else:
            for i in range(len(rest)):
                # make next
                next_val = soFar + rest[i]
                # make remaining
                remaining = rest[:i] + rest[i+1:]
                # recurse
                RecPermute(next_val, remaining)

    
    RecPermute("", s)

ListPermutations("abc")