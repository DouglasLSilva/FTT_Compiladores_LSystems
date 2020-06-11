import re 

class Grammar(object):

     def findAlphabet(self,arrayString):
        for string in arrayString:
            i = string.find('Σ :')
            if i != -1:
                alphabetString = string.replace('Σ :','').strip()
                alphabetArray =  alphabetString.split(',')
                alphabetArray = list(map(str.strip, alphabetArray))
                alphabetArray.remove('+')
                alphabetArray.remove('-')
                return alphabetArray

        return None

     def findSteps(self,arrayString):
        for string in arrayString:
            i = string.find('n :')
            if i != -1:
                return string.replace('n :','').strip()
            
        return None

     def findAxion(self,arrayString):
        for string in arrayString:
            i = string.find('ω :')
            if i != -1:
                return string.replace('ω :','').strip()
            
        return None

     def findAngle(self,arrayString):
        for string in arrayString:
            i = string.find('δ :')
            if i != -1:
                return string.replace('δ :','').strip().replace('º','')
            
        return None

     def findRules(self,arrayString):
          rules = []
          for string in arrayString:
               if(re.match('(p\d* :)',string)):
                   stringfix = string.replace('\n','').replace('→','->')
                   rules.append(re.sub('(p\d* :)','',stringfix))

          return rules

     def __init__(self, ArrayStringsOfTxt):
         self.alfabet = self.findAlphabet(ArrayStringsOfTxt)
         self.steps = self.findSteps(ArrayStringsOfTxt)
         self.axiom = self.findAxion(ArrayStringsOfTxt)
         self.angle = self.findAngle(ArrayStringsOfTxt)
         self.rules = self.findRules(ArrayStringsOfTxt)

