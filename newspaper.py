

def print_newspaper(lines, align, width):

    final_lines = []
    stars = "*" * (width + 2)
    final_lines.append(stars)

    for i, line in enumerate(lines):
        curr_line = []
        while line:
            if len(" ".join(curr_line + [line[0]])) <= width:
                curr_line.append(line.pop(0))

            else:
                words_to_add = " ".join(curr_line)
                spaces = " " * (width - len(words_to_add))
                
                if align[i] == "LEFT":
                    final_lines.append("*" + words_to_add + spaces + "*")
                else:
                    final_lines.append("*" + spaces + words_to_add + "*")
                
                curr_line = []

        words_to_add = " ".join(curr_line)
        spaces = " " * (width - len(words_to_add))
        
        if align[i] == "LEFT":
            final_lines.append("*" + words_to_add + spaces + "*")
        else:
            final_lines.append("*" + spaces + words_to_add + "*")


    final_lines.append(stars)

    for line in final_lines:
        print(line)



