# Perform context based predictions for people

male_pronoun_list = ["he", "him", "his"]
female_pronoun_list = ["she", "her", "hers"]
third_pronoun_list = ["they", "them", "their"]
male_student_list = ["Sayan","Clark","Bruce","Pablo","Than","Nick","Vennu","Pranav","Arnav","Josh"]
female_student_list = ["Wanda", "Wonder", "Ada", "Rachel", "Jennifer"]
pronoun_list = male_pronoun_list
for f in female_pronoun_list:
    pronoun_list.append(f)
for t in third_pronoun_list:
    pronoun_list.append(t)

def context_back(line_list):
    for l in range(len(line_list)):
        print(line_list[len(line_list)-l-1])
    first = line_list[0].split(" ")
    first = list(map(lambda x : x.lower(), first))
    pr = []
    ret = []
    for pron in pronoun_list:
        if pron in first:
            pr.append(pron)
    n = len(line_list)
    if len(pr) == 0:
        return []
    for pron in pr:
        check = True
        for i in range(n-1):
            for stud in female_student_list:
                if check and stud in line_list[i+1].split(" "):
                    if (pron in female_pronoun_list or pron in third_pronoun_list):
                        ret.append((pron, stud))
                        check = False
            for stud in male_student_list:
                if check and stud in line_list[i+1].split(" "):
                    if (pron in male_pronoun_list or pron in third_pronoun_list):
                        ret.append((pron, stud))
                        check = False
    return ret
