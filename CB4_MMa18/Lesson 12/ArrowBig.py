def stars(number_of_stars):
    answer=''
    for i in range( number_of_stars ):
        answer+='*'
    answer=answer.center(30)
    return answer

def arrow_head():
    for i in range(10):
        if(i == 0): print("*")
        else: print(stars(i*2))

arrow_head()

