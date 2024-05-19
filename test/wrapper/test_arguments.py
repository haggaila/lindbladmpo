# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Tests of the solver parameters handling.
"""

import unittest
import numpy as np
from lindbladmpo.LindbladMPOSolver import LindbladMPOSolver

# Defaults that should not interfere with the parameters check, are added just so we don't fail
# due to them being required arguments (don't have default values):
DEFAULT_TAU = 0.1
DEFAULT_T_FINAL = 20
DEFAULT_N = 10

s_output_path = "../"
s_cygwin_path = None
s_solver_path = None


# The following checks are named as follows:
# test_arg_<parameter being checked>_<Fail/Pass test><number of the test(if there are multiple)>
# example: test_arg_N_F1 means we are checking the parameter N and trying to make it fail

# Fail tests (trying to fail on purpose) should use assertNotEqual to ""
# Pass tests (trying to pass on purpose) should use assertEqual    to ""


class LindbladMPOSolverTestArguments(unittest.TestCase):
    """This class tests the handling of parameters by the solver."""

    def test_arg_N_F1(self):
        """Argument test."""
        parameters = {"N": "5", "t_final": DEFAULT_T_FINAL, "tau": DEFAULT_TAU}
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_N_F2(self):
        """Argument test."""
        parameters = {"N": -1, "t_final": DEFAULT_T_FINAL, "tau": DEFAULT_TAU}
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_N_P(self):
        """Argument test."""
        parameters = {"N": 20, "t_final": DEFAULT_T_FINAL, "tau": DEFAULT_TAU}
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_t_final_F1(self):
        """Argument test."""
        parameters = {"t_final": "20", "tau": DEFAULT_TAU, "N": DEFAULT_N}
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_t_final_P(self):
        """Argument test."""
        parameters = {"t_final": 20, "tau": DEFAULT_TAU, "N": DEFAULT_N}
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_t_init_P(self):
        """Argument test."""
        parameters = {"t_init": 10, "t_final": 20, "tau": DEFAULT_TAU, "N": DEFAULT_N}
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_tau_F1(self):
        """Argument test."""
        parameters = {"tau": "20", "N": DEFAULT_N, "t_final": DEFAULT_T_FINAL}
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_tau_F2(self):
        """Argument test."""
        parameters = {"tau": -20, "N": DEFAULT_N, "t_final": DEFAULT_T_FINAL}
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_tau_P(self):
        """Argument test."""
        parameters = {"tau": 20, "N": DEFAULT_N, "t_final": DEFAULT_T_FINAL}
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_l_x_F1(self):
        """Argument test."""
        parameters = {
            "l_x": 3.3,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_l_x_F2(self):
        """Argument test."""
        parameters = {
            "l_x": -4,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_l_x_P(self):
        """Argument test."""
        parameters = {
            "l_x": 4,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_l_y_F1(self):
        """Argument test."""
        parameters = {
            "l_y": 3.3,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_l_y_F2(self):
        """Argument test."""
        parameters = {
            "l_y": -4,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_l_y_P(self):
        """Argument test."""
        parameters = {
            "l_y": 4,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_output_step_F1(self):
        """Argument test."""
        parameters = {
            "output_step": 1.1,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_output_step_P(self):
        """Argument test."""
        parameters = {
            "output_step": 1,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_h_x_F1(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "h_x": "11",
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_h_x_F2(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "h_x": (1, 1),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_h_x_F3(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "h_x": np.zeros([5, 5]),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_h_x_F4(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "h_x": [1, 2, 3, 4],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_h_x_F5(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "h_x": [1, 2, 3, 4, "5"],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_h_x_F6(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "h_x": np.array([1, 2, 3, 4, 5, 6]),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_h_x_F7(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "h_x": np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_h_x_P1(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "h_x": [1, 2, 3, 4, 5],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_h_x_P2(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "h_x": np.array([1, 2, 3, 4, 5]),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_J_F1(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": [
                [2, 5, 6, "7", 9],
                [4.55, -4.1, 12, -33, 10],
                [4.55, -1.1, 17, 0, 10],
                [4.55, -4.1, 61, -33, 10],
                [4.55, -1.1, 11, -33, 10],
            ],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_J_F2(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": [
                [2, 5, 6, 5, 9],
                [4.55, -4.1, 12, -33, 10],
                [4.55, -4.1, 61, -33, 10],
                [4.55, -1.1, 11, -33, 10],
            ],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_J_F3(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": [
                [2, 5, 6, 7],
                [4.55, -4.1, 12, -33, 10],
                [4.55, -1.1, 17, 0, 10],
                [4.55, -4.1, 61, -33, 10],
                [4.55, -1.1, 11, -33, 10],
            ],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_J_F4(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_J_F5(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": np.array([[1, 2.0], [0, 0], (1 + 1, 3.0)]),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_J_F6(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": np.array(
                [
                    [1, 2, 3, 4, "P"],
                    [1, 2, 3, 4, 5],
                    [1, 2, 3, 4, 5],
                    [1, 2, 3, 4, 5],
                    [1, 2, 3, 4, 5],
                ]
            ),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_J_P_1(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": np.array(
                [
                    [1, 2, 3, 4, 3],
                    [1, 2, 3, 4, 5],
                    [1, 2, 3, 4, 5],
                    [1, 2, 3, 4, 5],
                    [1, 2, 3, 4, 5],
                ]
            ),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_J_P_2(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": -55,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_J_P_3(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": [
                [2, 5, 6, 7, -10],
                [4.55, -4.1, 12, -33, 10],
                [4.55, -1.1, 17, 0, 10],
                [4.55, -4.1, 61, -33, 10],
                [4.55, -1.1, 11, -33, 10],
            ],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_J_P_4(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": np.array(-55),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_J_P_5(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "J_z": np.zeros((5, 5)),
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_init_Pauli_state_F1(self):
        """Argument test."""
        parameters = {
            "init_product_state": "-a",
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_init_Pauli_state_F2(self):
        """Argument test."""
        parameters = {
            "init_product_state": -22,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_init_Pauli_state_P(self):
        """Argument test."""
        parameters = {
            "init_product_state": "-x",
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_b_periodic_x_F1(self):
        """Argument test."""
        parameters = {
            "b_periodic_x": -22,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_b_periodic_x_P(self):
        """Argument test."""
        parameters = {
            "b_periodic_x": False,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_trotter_order_F1(self):
        """Argument test."""
        parameters = {
            "trotter_order": 5,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_trotter_order_P(self):
        """Argument test."""
        parameters = {
            "trotter_order": 3,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_metadata_F1(self):
        """Argument test."""
        parameters = {
            "metadata": "CR/LF \n",
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_metadata_F2(self):
        """Argument test."""
        parameters = {
            "metadata": 0,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_cut_off_rho_F1(self):
        """Argument test."""
        parameters = {
            "cut_off_rho": [1, 1],
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_cut_off_rho_P(self):
        """Argument test."""
        parameters = {
            "cut_off_rho": 1.1e-199,
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_1q_components_F1(self):
        """Argument test."""
        parameters = {
            "1q_components": [1, 1],
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_1q_components_P(self):
        """Argument test."""
        parameters = {
            "1q_components": ["x", "y"],
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_1q_indices_F1(self):
        """Argument test."""
        parameters = {
            "1q_indices": [1, 1],
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_1q_indices_F2(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "1q_indices": [2, 5, 1],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_1q_indices_P(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "1q_indices": [2, 4, 1],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_2q_components_F1(self):
        """Argument test."""
        parameters = {
            "2q_components": ["xx", "xx"],
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_2q_components_F2(self):
        """Argument test."""
        parameters = {
            "2q_components": "xy",
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_2q_components_P1(self):
        """Argument test."""
        parameters = {
            "2q_components": ["XX", "XY", "XZ", "YY", "YZ", "ZZ"],
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_2q_components_P2(self):
        """Argument test."""
        parameters = {
            "2q_components": ["XX", "YY", "YZ", "ZZ"],
            "N": DEFAULT_N,
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_2q_indices_F1(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "2q_indices": [(1, 2), (3, 1), (2, 5), (3, 4)],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_2q_indices_F2(self):
        """Argument test."""
        parameters = {
            "N": 2,
            "2q_indices": [
                (1, 0),
                (2, 1),
                (2, 1),
                (0, 1),
                (1, 0),
                (2, 1),
                (2, 1),
                (0, 1),
            ],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertNotEqual(expected, out)

    def test_arg_2q_indices_P1(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "2q_indices": [(1, 2), (3, 1), (2, 4), (3, 4)],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_2q_indices_P2(self):
        """Argument test."""
        parameters = {
            "N": 5,
            "2q_indices": [(1, 2), (3, 4)],
            "t_final": DEFAULT_T_FINAL,
            "tau": DEFAULT_TAU,
        }
        expected = ""
        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertEqual(expected, out)

    def test_arg_1(self):
        """A multiple arguments test."""
        parameters = {}
        parameters["N"] = 5
        parameters["t_final"] = 20
        parameters["tau"] = 3
        parameters["output_step"] = 5

        parameters["h_x"] = 1.111
        parameters["h_y"] = [2.222, 4, 2e-2, 777777, -0.3]
        parameters["h_z"] = 3.333

        parameters["J"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 12, -33, 10],
            [4.55, -1.1, 17, 0, 10],
            [4.55, -4.1, 61, -33, 10],
            [4.55, -1.1, 11, -33, 10],
        ]

        parameters["J_z"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 12, -33, 10],
            [4.55, -1.1, 17, 0, 10],
            [4.55, -4.1, 61, -33, 10],
            [4.55, -1.1, 11, -33, 10],
        ]

        parameters["g_0"] = [2.222, 4, 2e-2, 777777, -0.3]
        parameters["g_1"] = np.array([1, 2, 3, 4, 5])
        parameters["g_2"] = -4e-10
        parameters["init_product_state"] = "+x"
        parameters["l_x"] = 5
        parameters["l_y"] = 1
        parameters["b_periodic_x"] = True
        parameters["b_periodic_y"] = False
        parameters["trotter_order"] = 3
        parameters["max_dim_rho"] = 200
        parameters["cut_off"] = 1e-10
        parameters["cut_off_rho"] = 1e-11
        parameters["b_force_rho_trace"] = False
        parameters["force_rho_hermitian_step"] = 1
        parameters["output_files_prefix"] = s_output_path
        parameters["metadata"] = "We agree to disagree."
        parameters["1q_components"] = ["x", "y", "z"]
        parameters["1q_indices"] = [1, 3, 4]
        parameters["2q_components"] = ["XX", "XY", "XZ", "YY", "YZ", "ZZ"]
        parameters["2q_indices"] = [(1, 2), (3, 1), (2, 4), (3, 4)]

        out = LindbladMPOSolver.verify_parameters(parameters)
        # this check should pass (no errors)
        self.assertTrue(out == "")

    def test_arg_2(self):
        """A multiple arguments test."""
        parameters = {}
        parameters["N"] = 5
        parameters["t_final"] = 9
        parameters["tau"] = 0.1

        parameters["h_x"] = 1.111
        parameters["h_y"] = [2.222, 4, 2e-2, 777777, -0.3]
        parameters["h_z"] = 3.333

        parameters["J_z"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 12, -33, 10],
            [4.55, -1.1, 17, 0],
            [4.55, -4.1, 61, -33, 10],
            [4.55, -1.1, 11, -33, 10],
        ]  # this should fail

        parameters["J"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 11, -33, 11e-9],
            [4.55, -2.1, 11, 0, 10],
            [6.25, -3.1, 2e-5, -33, 10],
        ]  # this should fail

        parameters["g_0"] = [2.222, 4, 777777, -0.3]  # this should fail
        parameters["g_1"] = -99
        parameters["g_2"] = "aaa"  # this should fail
        parameters["init_product_state"] = "-z"
        #    parameters['l_x'] =
        #    parameters['l_y'] =
        parameters["b_periodic_x"] = 0  # this should fail
        parameters["b_periodic_y"] = 1  # this should fail
        parameters["trotter_order"] = 3
        parameters["max_dim_rho"] = 200
        parameters["cut_off"] = 1e-10
        parameters["cut_off_rho"] = 1e-11
        parameters["b_force_rho_trace"] = "False"  # this should fail
        parameters["force_rho_hermitian_step"] = 1
        parameters["output_step"] = 0.6  # this should fail
        parameters["output_files_prefix"] = s_output_path
        parameters["1q_components"] = ["x", "y", "j"]  # this should fail
        parameters["1q_indices"] = [1, 3, 5]
        parameters["2q_components"] = [
            "XX",
            "XY",
            "A",
            "YY",
            "YZ",
            "ZZ",
        ]  # this should fail
        parameters["2q_indices"] = [(1, 2), (3, 5, 4), (2, 4)]  # this should fail

        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertTrue(out.count("Error") == 12)

    def test_arg_3(self):
        """A multiple arguments test."""
        parameters = {}
        parameters["N"] = 9
        parameters["t_final"] = "22"
        parameters["tau"] = "aaa"

        parameters["h_x"] = "aa1.111"
        parameters["h_y"] = "[2.222,       4,   2e-2, 777777,   -0.3]"
        parameters["h_z"] = "aa3.333"

        parameters["J_z"] = [
            [2, 5, 6, "7", 9],
            [4.55, -4.1, 12, -33, 10],
            [4.55, -1.1, 17, 0],
            [4.55, -4.1, 61, -33, 10],
            [4.55, -1.1, 11, -33, 10],
        ]

        parameters["J"] = [
            [2, 5, "6", 7, 9],
            [4.55, -4.1, 11, -33, 11e-9],
            [4.55, -2.1, 11, 0, 10],
            [6.25, -3.1, 2e-5, -33, 10],
        ]

        parameters["g_0"] = [2.222, 4]
        parameters["g_1"] = (-11, 22)
        parameters["g_2"] = "aaa"
        parameters["init_product_state"] = "+a2"

        parameters["b_periodic_x"] = 0
        parameters["b_periodic_y"] = 1
        parameters["trotter_order"] = (3.99, 99)
        parameters["max_dim_rho"] = 200.99
        parameters["cut_off"] = "1e-10"
        parameters["cut_off_rho"] = "1e-11"
        parameters["b_force_rho_trace"] = "False"
        parameters["force_rho_hermitian_step"] = "True"
        parameters["output_step"] = 0.6
        parameters["output_files_prefix"] = s_output_path
        parameters["1q_components"] = ["x", "y", "j"]
        parameters["1q_indices"] = [1, 3, 1, 5, 1]
        parameters["2q_components"] = ["XX", "XY", "A", "YY", "YZ", "ZZ"]
        parameters["2q_indices"] = [(1, 2), (3, 5, 4), (2, 4)]

        out = LindbladMPOSolver.verify_parameters(parameters)
        self.assertTrue(out.count("Error") == 24)

    def test_arg_4(self):
        """A multiple arguments test."""
        parameters = {}
        parameters["N"] = 5
        parameters["t_final"] = 20
        parameters["tau"] = 0.1

        parameters["h_x"] = 1.111
        parameters["h_y"] = [2.222, 4, 2e-2, 777777, -0.3]
        parameters["h_z"] = 3.333

        parameters["J_z"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 12, -33, 10],
            [4.55, -1.1, 17, 0, 10],
            [4.55, -4.1, 61, -33, 10],
            [4.55, -1.1, 11, -33, 10],
        ]

        parameters["J"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 11, -33, 11e-9],
            [4.55, -2.1, 11, 0, 10],
            [6.25, -3.1, 2e-5, -33, 10],
            [4.15, -4.1, 11, -33, 11],
        ]

        parameters["g_0"] = [2.222, 4, 2e-2, 777777, -0.3]
        parameters["g_1"] = -99
        parameters["g_2"] = -4e-10
        parameters["init_product_state"] = "-y"
        parameters["l_x"] = 1
        parameters["l_y"] = 5
        parameters["b_periodic_x"] = True
        parameters["b_periodic_y"] = False
        parameters["trotter_order"] = 3
        parameters["max_dim_rho"] = 200
        parameters["cut_off"] = 1e-10
        parameters["cut_off_rho"] = 1e-11
        parameters["b_force_rho_trace"] = False
        parameters["force_rho_hermitian_step"] = 1
        parameters["output_step"] = 1
        parameters["output_files_prefix"] = s_output_path
        parameters["1q_components"] = ["x", "y", "z"]
        parameters["1q_indices"] = [1, 3, 2]
        parameters["2q_components"] = ["XX", "XY", "XZ", "YY", "YZ", "ZZ"]
        parameters["2q_indices"] = [(1, 2), (3, 2), (2, 4)]

        out = LindbladMPOSolver.verify_parameters(parameters)
        # this check should pass (no errors)
        self.assertTrue(out == "")

    def test_arg_5(self):
        """A multiple arguments test."""
        parameters = {}
        parameters["N"] = 5
        parameters["t_final"] = 20
        parameters["tau"] = 0.1

        parameters["h_x"] = 1.111
        parameters["h_y"] = [2.222, 4, 2e-2, 777777, -0.3]
        parameters["h_z"] = 3.333

        parameters["J_z"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 12, -33, 10],
            [4.55, -1.1, 17, 0, 10],
            [4.55, -4.1, 61, -33, 10],
            [4.55, -1.1, 11, -33, 10],
        ]

        parameters["J"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 11, -33, 11e-9],
            [4.55, -2.1, 11, 0, 10],
            [6.25, -3.1, 2e-5, -33, 10],
            [4.15, -4.1, 11, -33, 11],
        ]

        parameters["g_0"] = [2.222, 4, 2e-2, 777777, -0.3]
        parameters["g_1"] = -99
        parameters["g_2"] = -4e-10
        parameters["init_product_state"] = "-x"
        #    parameters['l_x'] =
        #    parameters['l_y'] =
        parameters["b_periodic_x"] = True
        parameters["b_periodic_y"] = False
        parameters["trotter_order"] = 3
        parameters["max_dim_rho"] = 200
        parameters["cut_off"] = 1e-10
        parameters["cut_off_rho"] = 1e-11
        parameters["b_force_rho_trace"] = False
        parameters["force_rho_hermitian_step"] = 1
        parameters["output_step"] = 1
        parameters["output_files_prefix"] = s_output_path
        parameters["1q_components"] = ["x", "y", "z"]
        parameters["1q_indices"] = [1, 3, 99]
        parameters["2q_components"] = ["XX", "XY", "XZ", "YY", "YZ", "ZZ"]
        parameters["2q_indices"] = [(1, 2), (3, 1), (2, 4), (3, 4)]
        try:
            solver = LindbladMPOSolver(parameters, s_cygwin_path, s_solver_path)
            solver.build()
            self.assertTrue(False, "Test failed, expected to get an exception\n")
        except Exception:
            self.assertTrue(True)

    def test_arg_6(self):
        """A multiple arguments test."""
        parameters = {}
        parameters["N"] = 5
        parameters["t_final"] = 20
        parameters["tau"] = 0.1

        parameters["h_x"] = 1.111
        parameters["h_y"] = [2.222, 4, 2e-2, 777777, -0.3]
        parameters["h_z"] = 3.333

        parameters["J_z"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 12, -33, 10],
            [4.55, -1.1, 17, 0, 10],
            [4.55, -4.1, 61, -33, 10],
            [4.55, -1.1, 11, -33, 10],
        ]

        parameters["J"] = [
            [2, 5, 6, 7, 9],
            [4.55, -4.1, 11, -33, 11e-9],
            [4.55, -2.1, 11, 0, 10],
            [6.25, -3.1, 2e-5, -33, 10],
            [4.15, -4.1, 11, -33, 11],
        ]

        parameters["g_0"] = [2.222, 4, 2e-2, 777777, -0.3]
        parameters["g_1"] = -99
        parameters["g_2"] = -4e-10
        parameters["init_pauli_state"] = "+z"
        #    parameters['l_x'] =
        #    parameters['l_y'] =
        parameters["b_periodic_x"] = True
        parameters["b_periodic_y"] = False
        parameters["trotter_order"] = 3
        parameters["max_dim_rho"] = 200
        parameters["cut_off"] = 1e-10
        parameters["cut_off_rho"] = 1e-11
        parameters["b_force_rho_trace"] = False
        parameters["force_rho_hermitian_step"] = 1
        parameters["output_step"] = 1
        parameters["output_files_prefix"] = s_output_path
        parameters["1q_components"] = ["x", "y", "z"]
        parameters["1q_indices"] = [1, 2, 4]
        parameters["2q_components"] = ["XX", "XY", "XZ", "YY", "YZ", "ZZ"]
        parameters["2q_indices"] = [(1, 2), (3, 1), (2, 4), (3, 4)]
        try:
            solver = LindbladMPOSolver(parameters, s_cygwin_path, s_solver_path)
            solver.build()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False, "Test failed, exception was not expected")


if __name__ == "__main__":
    unittest.main()
