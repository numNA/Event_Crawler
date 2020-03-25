

from coex import get_events as cx_evt
from kintex import get_events as KT
#from so import get_jobs as so_job
from save import save_to_file
# print(ind_job())

# cx_evt()
KT = KT()
CX = cx_evt()
# print(CX)
EV = KT + CX
save_to_file(EV)
print("Complete scrapping and saving the csv file!")


#Indeed = ind_job()
#SO = so_job()
#jobs = Indeed + SO
# save_to_file(jobs)
