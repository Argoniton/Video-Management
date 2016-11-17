def dictionaryToXML(dictionary):
    returnXML = ''
    def next(n, dictionary):
        returnElement = ''
        for e in dictionary.keys():
            if type(dictionary[e]) == type({}):
                returnElement += '{}<dictionary title="{}">'.format('  '*n,e) + '\n'
                returnElement += next(n + 1, dictionary[e])
                returnElement += '{}</dictionary>'.format('  '*n) + '\n'
            else:
                returnElement += '{}<element title="{}">'.format('  '*n, e) + str(dictionary[e]) + '</element>' + '\n'
        return returnElement
    returnXML += '<?xml version="1.0" encoding="UTF-8"?>' + '\n'
    returnXML += '<top>' + '\n'
    returnXML += next(1, dictionary)
    returnXML += '</top>' + '\n'
    return returnXML
if __name__ == '__main__':
    d = {'a':3, 'b':{1:2, 3:4}}
    print(dictionaryToXML(d))
