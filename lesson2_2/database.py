class Simpledb():
    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                " filename=" + str(self.filename) +
                ">")

    def insert(self, key, value):
        f = open(self.filename, 'a')
        f.write(key.strip().lower() + '\t' + value.strip().lower() + '\n')
        f.close

    def select_one(self, key):
        f = open(self.filename, 'r')
        status = ''
        for row in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                return v[:-1]
                status = 'found'
        if status != 'found':
            print('Name not in database')
            import time
            time.sleep(0.5)
        if status == 'found':
            print(value + ' is the value of  ' + key)
        f.close()

    def delete(self, key):
        status = ''
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for row in f:
            (k, v) = row.split('\t', 1)
            if k != key:
                result.write(row)
            elif k == key:
                pass
                #status = 'found'
        #if status != 'found':
        #   print('The name is not in the database')
        #   import time
        #   time.sleep(0.5)
        f.close()
        import os
        result.close()
        os.replace('result.txt', self.filename)

    def update(self, key, value):
        status = ''
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                result.write(key + '\t' + value + '\n')
                status = 'found'
            else:
                result.write(row)
        if status != 'found':
            print('That name is not in the database')
            print('Please try again with a name in the database inorder to update it')
            import time
            time.sleep(0.5)
        f.close()
        import os
        result.close()
        os.replace('result.txt', self.filename)



