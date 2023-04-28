# -*- coding: utf-8 -*-
import datetime
from dateutil.relativedelta import relativedelta
import subprocess

start_date = datetime.date(2015, 1, 1)
end_date = datetime.date(2015, 4, 17)

delta = relativedelta(months=1)
while start_date <= end_date:
    date_str = start_date.strftime("%Y%m%d")
    # perl_script = "C:/Users/kongdeyin/Desktop/his_kdy_pef_lk_pax_flown_sum0300.pl"
    perl_script = "C:/Users/kongdeyin/Desktop/his_kdy_pef_lk_pax_flown_sum_old0300.pl"
    subprocess.call(["perl", perl_script, date_str])
    start_date += delta