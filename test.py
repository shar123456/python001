import time
from tushare import get_realtime_quotes
from DbCore.personService import *
#for x in range(5):
 #print("我爱你中国！")
 #time.sleep(1)
#datas =get_realtime_quotes("600745")
#print(datas)



def main():
    person=Person()
    #person.getPersonsById()
    person.addPerson()
    person.getAllPersons()
    person.closeConn()


if __name__=='__main__':
    main()
