d=  {
        100:(
                10,
                "python",
                "helloworld",
                ("django framework",),
                {
                    'bat':  [
                                'c programming',
                                'java',
                                'c++',
                                'r language'
                            ]
                },
                (
                    10,
                    20
                )
            ),
            'apple':{
                        'venugopal',
                        'pooja',
                        'kasinath'
                    },
            'Z':'pyspiders'
    }
print("1, "+d[100][3][0])
print("2, "+d[100][3][0][::2])
print("3, "+d[100][3][0][::-2])
print("4, "+str(set(d[100][4]['bat'][::-1])))
print("5, "+str(set(d[100][4]['bat'][::-3])))

print("6, "+str(set(list(d.keys())[::1])))
print("7, "+str(set(d.keys())))

print("8, "+d[100][2][::-1])
print("9, "+d[100][4]['bat'][0][:1:-1])
print("10, "+d[100][4]['bat'][0][::-3])


ans=[]
for i in d['apple']:
    ans.append(i[::-1])
print("11, "+str(set(ans)))


ans=[]
for i in d[100][4]['bat'][1:3]:
    ans.append(i[::-1])
print("12, "+str(set(ans)))

