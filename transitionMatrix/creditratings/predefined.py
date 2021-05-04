# encoding: utf-8

# (c) 2017-2021 Open Risk, all rights reserved
#
# TransitionMatrix is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of TransitionMatrix. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# Matrix used in the seminal JLT Paper
# Jarrow, Lando, Turnbull A Markov Model for the Term Structure of Credit Spread
# Review of Financial Studies, 1997 Vol 10
# Based on S&P average 1-year transitions probabilities 1981-1991

JLT = [[0.8910, 0.0963, 0.0078, 0.0019, 0.0030, 0.0000, 0.0000, 0.0000],
       [0.0086, 0.9010, 0.0747, 0.0099, 0.0029, 0.0029, 0.0000, 0.0000],
       [0.0009, 0.0291, 0.8894, 0.0649, 0.0101, 0.0045, 0.0000, 0.0009],
       [0.0006, 0.0043, 0.0656, 0.8427, 0.0644, 0.0160, 0.0018, 0.0045],
       [0.0004, 0.0022, 0.0079, 0.0719, 0.7764, 0.1043, 0.0127, 0.0241],
       [0.0000, 0.0019, 0.0031, 0.0066, 0.0517, 0.8246, 0.0435, 0.0685],
       [0.0000, 0.0000, 0.0116, 0.0116, 0.0203, 0.0754, 0.6493, 0.2319],
       [0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 1.0000]]

# Standard & Poor's Average One-Year Transition Rates For Global Corporates By Rating Modifier (1981 - 2016)

SP17 = [
    [0.8705, 0.0578, 0.0256, 0.0069, 0.0016, 0.0024, 0.0013, 0, 0.0005, 0, 0.0003, 0.0005, 0, 0, 0.0003, 0, 0.0005, 0],
    [0.0242, 0.7753, 0.1154, 0.0378, 0.0076, 0.004, 0.002, 0.0005, 0.001, 0.0005, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.0044, 0.0129, 0.8025, 0.0871, 0.0283, 0.0121, 0.0039, 0.004, 0.0013, 0.0008, 0.0005, 0.0003, 0.0002, 0.0002, 0,
     0.0002, 0.0005, 0.0002],
    [0.0004, 0.0012, 0.0397, 0.7801, 0.1007, 0.0234, 0.0061, 0.0028, 0.0016, 0.0007, 0.0003, 0, 0, 0.0003, 0.0009, 0, 0,
     0.0003],
    [0, 0.0006, 0.0048, 0.0458, 0.7751, 0.091, 0.0229, 0.0066, 0.0035, 0.0009, 0.0006, 0.001, 0.0001, 0.0007, 0.0003, 0,
     0, 0.0005],
    [0.0004, 0.0005, 0.0024, 0.0046, 0.0526, 0.7804, 0.0704, 0.0257, 0.0093, 0.0029, 0.0012, 0.0011, 0.0008, 0.001,
     0.0002, 0, 0.0002, 0.0006],
    [0.0004, 0.0001, 0.0007, 0.0017, 0.0048, 0.0672, 0.7684, 0.0762, 0.0222, 0.0062, 0.0015, 0.0015, 0.0013, 0.0012,
     0.0003, 0.0001, 0.0003, 0.0007],
    [0, 0.0001, 0.0006, 0.0007, 0.0023, 0.0086, 0.0726, 0.744, 0.0841, 0.018, 0.0041, 0.0034, 0.0015, 0.0018, 0.0012,
     0.0003, 0.0007, 0.0012],
    [0.0001, 0.0001, 0.0005, 0.0003, 0.0011, 0.0034, 0.0112, 0.0768, 0.7501, 0.0641, 0.0141, 0.0066, 0.003, 0.0025,
     0.0013, 0.0004, 0.0006, 0.0017],
    [0.0001, 0.0001, 0.0002, 0.0005, 0.0006, 0.0016, 0.0031, 0.0126, 0.0911, 0.7163, 0.0585, 0.0218, 0.0092, 0.0041,
     0.0025, 0.0017, 0.0023, 0.0026],
    [0.0005, 0, 0, 0.0003, 0.0002, 0.001, 0.0008, 0.0046, 0.0184, 0.1151, 0.6356, 0.078, 0.0295, 0.0104, 0.0065, 0.0026,
     0.0043, 0.0036],
    [0, 0, 0.0004, 0.0001, 0, 0.0007, 0.0005, 0.0019, 0.0056, 0.0226, 0.0967, 0.6474, 0.0813, 0.0234, 0.0107, 0.0035,
     0.006, 0.0058],
    [0, 0, 0, 0.0001, 0.0001, 0.0001, 0.0005, 0.0011, 0.0025, 0.0039, 0.0187, 0.0934, 0.6309, 0.0864, 0.0319, 0.0083,
     0.0075, 0.0105],
    [0, 0.0001, 0, 0.0003, 0, 0.0003, 0.0007, 0.0005, 0.0006, 0.0012, 0.0031, 0.0151, 0.0807, 0.6314, 0.0891, 0.0255,
     0.0176, 0.0215],
    [0, 0, 0.0001, 0.0001, 0, 0.0004, 0.0005, 0.0002, 0.0007, 0.0004, 0.0014, 0.0026, 0.0128, 0.0794, 0.6136, 0.0855,
     0.0417, 0.0389],
    [0, 0, 0, 0, 0.0002, 0.0004, 0, 0.0008, 0.0006, 0.0012, 0.001, 0.0018, 0.0047, 0.0232, 0.1016, 0.5336, 0.1177,
     0.0749],
    [0, 0, 0, 0, 0.0003, 0, 0.001, 0.0006, 0.0006, 0.0006, 0.0003, 0.0016, 0.0044, 0.0108, 0.0273, 0.0911, 0.4397,
     0.2678]]

# A Generic matrix with 7 non-absorbing and one absorbing state

Generic = [
    [0.92039, 0.0709, 0.0063, 0.0015, 0.0006, 0.0002, 0.0001, 1e-05],
    [0.0062, 0.9084, 0.0776, 0.0059, 0.0006, 0.001, 0.0002, 0.0001],
    [0.0005, 0.0209, 0.9138, 0.0579, 0.0044, 0.0016, 0.0004, 0.0005],
    [0.0004, 0.0021, 0.041, 0.8936, 0.0482, 0.0086, 0.0024, 0.0037],
    [0.0003, 0.0008, 0.014, 0.0553, 0.8225, 0.0815, 0.0111, 0.0145],
    [0.0001, 0.0004, 0.0057, 0.0134, 0.0539, 0.8114, 0.0492, 0.0659],
    [1e-05, 0.0002, 0.0029, 0.0058, 0.0155, 0.1054, 0.52879, 0.3414],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]

# A Minimal matrix with an absorbing state
# In credit context it emulates Investment Grade / Subinvestment Grade / Default states
# or IFRS 9 Stage 1 / Stage 2 / Stage 3 states

Minimal = [
    [0.8, 0.15, 0.05],
    [0.15, 0.7, 0.15],
    [0.0, 0.0, 1.0]
]

# SP 2002 Matrix with and without NR state

SP02NR = [
    [89.37, 6.04, 0.44, 0.14, 0.05, 0.0, 0.00, 0.00, 3.97],
    [0.57, 87.76, 7.3, 0.59, 0.06, 0.11, 0.02, 0.01, 3.58],
    [0.05, 2.01, 87.62, 5.37, 0.45, 0.18, 0.04, 0.05, 4.22],
    [0.03, 0.21, 4.15, 84.44, 4.39, 0.89, 0.26, 0.37, 5.26],
    [0.03, 0.08, 0.4, 5.5, 76.44, 7.14, 1.11, 1.38, 7.92],
    [0, 0.07, 0.26, 0.36, 4.74, 74.12, 4.37, 6.20, 9.87],
    [0.09, 0.0, 0.28, 0.56, 1.39, 8.8, 49.72, 27.87, 11.30],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0]
]

SP02 = [
    [93.06, 6.29, 0.45, 0.14, 0.06, 0.00, 0.00, 0.00],
    [0.59, 90.99, 7.59, 0.61, 0.06, 0.11, 0.02, 0.01],
    [0.05, 2.11, 91.43, 5.63, 0.47, 0.19, 0.04, 0.05],
    [0.03, 0.23, 4.44, 88.98, 4.70, 0.95, 0.28, 0.39],
    [0.04, 0.09, 0.44, 6.07, 82.73, 7.89, 1.22, 1.53],
    [0.00, 0.08, 0.29, 0.41, 5.32, 82.06, 4.90, 6.95],
    [0.10, 0.0, 0.31, 0.63, 1.57, 9.97, 55.82, 31.58],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0]
]

# TODO Additional credit migration matrices

TestCase = [
    [0.9302113, 0.0132872, 0.0071951, 0.0003966, 0.0001883, 0.0001850, 0.0001163, 0.0001065, 0.0483137],
    [0.0120166, 0.8834034, 0.0649207, 0.0036649, 0.0002824, 0.0001747, 0.0000904, 0.0000781, 0.0353688],
    [0.0010724, 0.0232585, 0.8865029, 0.0477676, 0.0032491, 0.0010507, 0.0002062, 0.0000968, 0.0367958],
    [0.0000198, 0.0005074, 0.0341779, 0.8599584, 0.0522125, 0.0151643, 0.0032330, 0.0004825, 0.0342442],
    [0.0000037, 0.0002268, 0.0057361, 0.0760668, 0.7367912, 0.1053950, 0.0171777, 0.0044551, 0.0541476],
    [0.0000095, 0.0012905, 0.0017833, 0.0113293, 0.0716062, 0.7554586, 0.0770091, 0.0224190, 0.0590945],
    [0.0000018, 0.0003380, 0.0008636, 0.0109581, 0.0214451, 0.0893430, 0.6019427, 0.1032959, 0.1718118],
    [0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 1.0000000, 0.0000000],
    [0.0000209, 0.0027540, 0.0056307, 0.0079146, 0.0069479, 0.0071931, 0.0044121, 0.0043707, 0.9607560]
]
