#1- school maintains student grades in 3 subjects. waf to calculate the avg marks.
#  show how defulat parameters could bbe used if a stuent has missed a test assuming marks=0


def average(s1=0, s2=0, s3=0):
    sum= s1+s2+s3
    avg= sum/3
    return avg

ans= average(s1=50, s2=70)
print(ans)

