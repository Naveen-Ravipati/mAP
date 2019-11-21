def analysis(filename):
    file = open(filename)
    total = []
    for entry in file:
        info = entry.split(' ')
        total.append(info)
    total.sort(key = lambda x: int(x[1][:-1]),reverse=True)
    # print(total[:1000])
    final_analysis = open('final_analysis.txt','w')
    for entry in total:
        final_analysis.write(' '.join(entry))
    final_analysis.close()

filename = 'analysis.txt'
analysis(filename)
