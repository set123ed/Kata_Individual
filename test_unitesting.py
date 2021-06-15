import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    
    def test_findvocals(self):
        truthdata = "a || b && !c"
        uniquelist = []
        for x in truthdata:
            if x not in uniquelist:
                uniquelist.append(x)
        self.assertTrue(str(uniquelist))

    def test_countvocals(self):
        enouns = "a || b && !c"
        enouns = enouns.replace("&&","")
        enouns = enouns.replace("||","")
        enouns = enouns.replace("^","")
        enouns = enouns.replace("!","")
        enouns = enouns.replace(" ","")
        uniquelist = []
        count = 0
        for x in enouns:
            if x not in uniquelist:
                uniquelist.append(x)
        for i in uniquelist:
            count += 1

        self.assertEquals(3,count)
    
    def test_truthtable(self):
        enouns = "a || b && !c"
        uniquelist = ['a','b','c']
        enouns = enouns.replace(uniquelist[0],"a")
        enouns = enouns.replace(uniquelist[1], "b")
        self.assertEqual("b",uniquelist[0])

    def test_countlines(self):
        enouns = "a | b & ~c"
        countlines = 0
        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):
                    x = eval(enouns)
                    (str(a) + "\t"  + str(b) +"\t" + str(c) + "\t"+ str(x))
                    countlines += 1
        self.assertFalse(countlines>2)


