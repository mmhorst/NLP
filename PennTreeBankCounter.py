import re
with open("test.txt", "r") as f:
    lines = f.readlines()

    # initialize structures to hold paren stack and constituents found within VP
    tl = []
    d = {}
    v_stack = []
    constituent_stack = []
    in_VP = False

    # loop over lines in file; tokenize
    for line in lines:
        verb = re.compile(r'\(VP [^\(]*\)')
        if re.search(verb, line):
            d["IVP"] = d.get('IVP', 0) + 1
        line = str(line)
        line = line.replace("(", " ( ")
        line = line.replace(")", " ) ")
        for l in line.split():
            tl.append(l)

    # loop over tokens
    for line in tl:
        if in_VP:        
            if line == '(':
                v_stack.append(line)
            elif line == ')':
                v_stack = v_stack[0:-1]
                if len(v_stack) == 0:  # then we've reached end of VP
                    # check constituent_stack
                    if len(constituent_stack) == 2:
                        if constituent_stack[0] == "NP":
                            if constituent_stack[1] == "NP":
                                d["DVP"] = d.get("DVP", 0) + 1
                    else:
                        # didn't find a DVP or IVP
                        pass 
                    constituent_stack = []
                    in_VP = False
            elif len(v_stack) == 2:
            # if theres only the opening brace of VP and potential NP in v_stack
                if line == "NP":
                    constituent_stack.append(line)
                elif line == "VP":
                    constituent_stack = []
                else:
                # if it doesn't match, fooey
                    pass       
            elif line == "VP":
                constituent_stack = []
                
        if line == 'NP':
            d['NP'] = d.get('NP', 0) + 1
        if line == 'S':
            d['S'] = d.get('S', 0) + 1
        if line == 'VP':
            v_stack = []
            v_stack.append('(')
            in_VP = True
            d['VP'] = d.get('VP', 0) + 1

    for k in d.keys():
        print(k, "\t" + str(d[k]))
		
