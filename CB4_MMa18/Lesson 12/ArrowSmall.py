def stars(number_of_stars):
    answer=''
    for i in range( number_of_stars ):
        answer+='*'
    answer=answer.center(30)
    return answer

##print( stars(1) )
##print( stars(3) )
##print( stars(5) )
##print( stars(5) )
##print( stars(3) )
##print( stars(1) )

for i in range(1,6,2):
    print(stars(i))

for i in range(5,0,-2):
    print(stars(i))

