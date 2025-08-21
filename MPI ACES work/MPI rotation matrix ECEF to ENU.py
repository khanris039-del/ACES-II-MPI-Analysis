import numpy as np
import spaceToolsLib

# WGS84 constants
a = 6378137.0                # semi-major axis (m)
b = 6356752.314245          # semi-minor axis
f = (a - b) / a       # flattening of ellipsodi
e2 = f * (2 - f)              # eccentricity squared

# ref point in geodetic coordinates (degrees, meters)
lat0, lon0, h0 = np.radians([45.0, 90.0, 0.0])

# ref piont in ECEF
N = a / np.sqrt(1 - e2 * np.sin(lat0)**2)
ref_ecef = np.array([
    (N + h0) * np.cos(lat0) * np.cos(lon0),
    (N + h0) * np.cos(lat0) * np.sin(lon0),
    (N * (1 - e2) + h0) * np.sin(lat0)
])

# rot matrix ECEF -> ENU
R = np.array([
    [-np.sin(lon0),               np.cos(lon0),              0],
    [-np.sin(lat0)*np.cos(lon0), -np.sin(lat0)*np.sin(lon0), np.cos(lat0)],
    [ np.cos(lat0)*np.cos(lon0),  np.cos(lat0)*np.sin(lon0), np.sin(lat0)]
])

a = spaceToolsLib.ENUtoECEF(45, 90)

# for ENU -> ECEF, apply arr.T to rotation matrix to get the transpose

# test: 1000 m east in ENU
enu_test = np.array([1000.0, 0.0, 0.0])
test_ecef = ref_ecef + R.T @ enu_test
enu_computed = R @ (test_ecef - ref_ecef)

print("ref ECEF:", ref_ecef)
print("test ECEF:", test_ecef)
print("ENU Computed:", enu_computed)
print("difference :", enu_computed - enu_test)
print(a)
