import time
import schedule

def executar():
    print('Executou\n')
i=1
schedule.every(10).seconds.do(executar)
while True:
    print('Ciclo',i)
    i= i+1
    schedule.run_pending()
    time.sleep(1)