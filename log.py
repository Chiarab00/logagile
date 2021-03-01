import logging
import array
import unittest
class Debug:
    def __init__(self, string):
        self.string=string

    def getlogs(self):
        array=self.string
        array1=[] 
        for x in range(len(array)): 
            if  array[x] != "" and array[x] != " ":
                array1.append(array[x])
            else:
                x=x+1
        if len(array1)==0 and (array[0]== "" or array[0]== " " ):
            return "Errore"
        else:
            return (array1)
    def getlogstofile(self):
        array=self.string
        array1=[] 
        f = open("log.txt", "w") 
        for x in range(len(array)): 
            if  array[x] != "" and array[x] != " ":
                array1.append(array[x])
                
            else:
                x=x+1
        f.write(str(array1))           
        f.close() 
   
        
   
Deb1 = Debug([""])
print(Debug.getlogs(Deb1))
Debug.getlogstofile(Deb1)


class DebugTest(unittest.TestCase): 
    
    def error_string_space(self):
        msg=" "   
        self.assertEqual(Debug.getlogs(msg), 'Errore')
    def error_string_null(self):
        msg=""   
        self.assertEqual(Debug.getlogs(msg), 'Errore')

if __name__ == '__main__':
    unittest.main()