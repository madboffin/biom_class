import matplotlib.pyplot as plt
import numpy as np

from gait_functions import *
from btkTools import *

# === detecting the HJC using Hara's algorithm ===

file_cali='JuanDR_Calib01.c3d'
file_walk='JuanDR_Walk01.c3d'

# leg length from calibration file
acq = smartReader(file_cali)
fs = acq.GetPointFrequency()
# print(getMarkerNames(acq))

# relevant markers
rmed = acq.GetPoint("RMED").GetValues()
lmed = acq.GetPoint("LMED").GetValues()
lasi = acq.GetPoint("LASI").GetValues()
rasi = acq.GetPoint("RASI").GetValues()

# leg length
LLL = get_leglen(lmed, lasi)
LLR = get_leglen(rmed, rasi)
print(f'Leg length: left {LLL:.2f} mm, right {LLR:.2f} mm')


# finding HJCs in walking file
acq = smartReader(file_walk)
fs = acq.GetPointFrequency()

# relevant markers
sacr = acq.GetPoint("SACR").GetValues()
rmed = acq.GetPoint("RMED").GetValues()
lmed = acq.GetPoint("LMED").GetValues()
lasi = acq.GetPoint("LASI").GetValues()
rasi = acq.GetPoint("RASI").GetValues()

# append middle point of asis to acquisition object
mid_asi = (lasi + rasi) / 2

# reference vectors
Y0 = normalize_vector( rasi-mid_asi )                    # mid-right  (Medial-lateral direction)
Z0 = normalize_vector( np.cross(lasi-rasi, sacr-rasi) )  # bottom-up  (Inferior-superior direction)
X0 = np.cross(Z0, Y0)                                    # back-front (posterior-anterior direction)
# print(X0.shape, X0)

# hip joint centre left side
HJC_estimate = get_hjc(LLL)
HJCx_L = X0 * HJC_estimate[0]
HJCy_L = Y0 * HJC_estimate[1]
HJCz_L = Z0 * HJC_estimate[2]
# print(HJC_estimate)

# hip joint centre right side
HJC_estimate = get_hjc(LLR)
HJCx_R = X0 * HJC_estimate[0]
HJCy_R = -Y0 * HJC_estimate[1]
HJCz_R = Z0 * HJC_estimate[2]

# moving coordinates to moving body
HJC_L = mid_asi + HJCx_L + HJCy_L + HJCz_L
HJC_R = mid_asi + HJCx_R + HJCy_R + HJCz_R

# adding HJC points to acquisition object
smartAppendPoint(acq, "HJC_L", HJC_L)
smartAppendPoint(acq, "HJC_R", HJC_R)

# writing new c3d file
new_file_name = f"{file_walk[:-4]}_with_HJC.c3d"
print(f"Saving .c3d file as {new_file_name}")

smartWriter(acq, new_file_name)
