import numpy as py
import PyRth

from measurement_data import (
    MOSFET_CALIB_DATA,
    MOSFET_DRY_DATA,
    TEMP_DATA,
    MY_DATA
)


params = {
                "data": MY_DATA, # insert numpy array with test data here
                "output_dir": "output",
                "label": "MOSFET_tim_sobhy",
                "input_mode": "temp",#There's also a temperature mode, but not needed
                "deconv_mode": "bayesian",#More methods
                "bay_steps": 1000,
                "struc_method": "sobhy",#More methods
                "lower_fit_limit": 5e-4,
                "upper_fit_limit": 1e-3,
                "extrapolate": True #Extrapolate used to determine initial temp of die
                #"calib": MOSFET_CALIB_DATA # insert numpy array with calibration data here
                #"power_step": 540
            }

        
"""params= {
            "data": MY_DATA,
            "output_dir": "output/basic_test",
            "label": "TEMP_lasso",
            "input_mode": "temp",
            "extrapolate": False,
            "deconv_mode": "lasso",
            "struc_method": "sobhy",
            "data_cut_lower": 500,
            "data_cut_upper": float("inf"),
            "temp_0_avg_range": (501, 513),
        }"""

eval_instance = PyRth.Evaluation()
modules = eval_instance.standard_module(params)
#eval_instance.save_as_csv()
#eval_instance.save_figures()
eval_instance.save_all()
a = modules.cau_res
Cauer_model_f = open("output/Cauer.csv", "w")
Cauer_model_f.write(py.array2string(a, None, None, None, "\n"))