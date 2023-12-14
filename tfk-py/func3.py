def fun(name, **data):
    print(name)
    
    for i,j in data.items():
        print(i,j)

fun('Taofeek', age=28, city='Nigeria', mob=9063659635)
