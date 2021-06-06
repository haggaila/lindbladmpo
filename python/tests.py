from MPOLindbladSolver import MPOLindbladSolver

import numpy as np
import unittest


# space holders that should not interfere with the parameters check, are added just so we don't fail
# on the demand to have then in every run (don't have default values):
SH_TAU = 0.1
SH_T_FINAL = 20
SH_N = 10


# The following checks are named like so:
# arg_check_<parameter being checked>_<Fail/Pass test><number of the test(if there are multiple)>
# example: arg_check_N_F1 means we are checking the parameter N and trying to make it fail

# Fail tests (trying to fail on purpose) should use assertNotEqual to ""
# Pass tests (trying to pass on purpose) should use assertEqual    to ""

class TestArgs(unittest.TestCase):
    def arg_check_N_F1(self):
        input_dict = {'N': "5", 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_N_F2(self):
        input_dict = {'N': -1, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_N_P(self):
        input_dict = {'N': 20, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_t_final_F1(self):
        input_dict = {'t_final': "20", 'tau': SH_TAU, 'N': SH_N}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_t_final_F2(self):
        input_dict = {'t_final': -20, 'tau': SH_TAU, 'N': SH_N}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_t_final_P(self):
        input_dict = {'t_final': 20, 'tau': SH_TAU, 'N': SH_N}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_tau_F1(self):
        input_dict = {'tau': "20", 'N': SH_N, 't_final': SH_T_FINAL}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_tau_F2(self):
        input_dict = {'tau': -20, 'N': SH_N, 't_final': SH_T_FINAL}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_tau_P(self):
        input_dict = {'tau': 20, 'N': SH_N, 't_final': SH_T_FINAL}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_l_x_F1(self):
        input_dict = {'l_x': 3.3, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_l_x_F2(self):
        input_dict = {'l_x': -4, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_l_x_P(self):
        input_dict = {'l_x': 4, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_l_y_F1(self):
        input_dict = {'l_y': 3.3, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_l_y_F2(self):
        input_dict = {'l_y': -4, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_l_y_P(self):
        input_dict = {'l_y': 4, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_output_step_F1(self):
        input_dict = {'output_step': 1.1, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_output_step_P(self):
        input_dict = {'output_step': 1, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_h_x_F1(self):
        input_dict = {'N': 5, 'h_x': "11", 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_h_x_F2(self):
        input_dict = {'N': 5, 'h_x': (1, 1), 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_h_x_F3(self):
        input_dict = {'N': 5, 'h_x': np.zeros([5, 5]), 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_h_x_F4(self):
        input_dict = {'N': 5, 'h_x': [1, 2, 3, 4], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_h_x_F5(self):
        input_dict = {'N': 5, 'h_x': [1, 2, 3, 4, '5'], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_h_x_F6(self):
        input_dict = {'N': 5, 'h_x': np.array([1, 2, 3, 4, 5, 6]), 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_h_x_F7(self):
        input_dict = {'N': 5, 'h_x': np.array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_h_x_P1(self):
        input_dict = {'N': 5, 'h_x': [1, 2, 3, 4, 5], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_h_x_P2(self):
        input_dict = {'N': 5, 'h_x': np.array([1, 2, 3, 4, 5]), 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_J_F1(self):
        input_dict = {'N': 5, 'J_z': [[2, 5, 6, '7', 9],
                                      [4.55, -4.1, 12, -33, 10],
                                      [4.55, -1.1, 17, 0, 10],
                                      [4.55, -4.1, 61, -33, 10],
                                      [4.55, -1.1, 11, -33, 10]], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_J_F2(self):
        input_dict = {'N': 5, 'J_z': [[2, 5, 6, 5, 9],
                                      [4.55, -4.1, 12, -33, 10],
                                      [4.55, -4.1, 61, -33, 10],
                                      [4.55, -1.1, 11, -33, 10]], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_J_F3(self):
        input_dict = {'N': 5, 'J_z': [[2, 5, 6, 7],
                                      [4.55, -4.1, 12, -33, 10],
                                      [4.55, -1.1, 17, 0, 10],
                                      [4.55, -4.1, 61, -33, 10],
                                      [4.55, -1.1, 11, -33, 10]], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_J_F4(self):
        input_dict = {'N': 5, 'J_z': np.array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_J_F5(self):
        input_dict = {'N': 5, 'J_z': np.array([1, 2, 3, 4, "pp"],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5]), 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_J_P_1(self):
        input_dict = {'N': 5, 'J_z': np.array([1, 2, 3, 4, 3],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5]), 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_J_P_2(self):
        input_dict = {'N': 5, 'J_z': -55, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_J_P_3(self):
        input_dict = {'N': 5, 'J_z': [[2, 5, 6, 7, -10],
                                      [4.55, -4.1, 12, -33, 10],
                                      [4.55, -1.1, 17, 0, 10],
                                      [4.55, -4.1, 61, -33, 10],
                                      [4.55, -1.1, 11, -33, 10]], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_J_P_4(self):
        input_dict = {'N': 5, 'J_z': np.array(-55), 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_init_Pauli_state_F1(self):
        input_dict = {'init_Pauli_state': "-a", 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_init_Pauli_state_F2(self):
        input_dict = {'init_Pauli_state': -22, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_init_Pauli_state_P(self):
        input_dict = {'init_Pauli_state': "-x", 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_b_periodic_x_F1(self):
        input_dict = {'b_periodic_x': -22, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_b_periodic_x_P(self):
        input_dict = {'b_periodic_x': False, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_trotter_order_F1(self):
        input_dict = {'trotter_order': 5, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_trotter_order_P(self):
        input_dict = {'trotter_order': 3, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_max_dim_F1(self):
        input_dict = {'max_dim': 5.1, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_max_dim_P(self):
        input_dict = {'max_dim': 1, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_cut_off_rho_F1(self):
        input_dict = {'cut_off_rho': [1, 1], 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_cut_off_rho_P(self):
        input_dict = {'cut_off_rho': 1.1e-199, 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_1q_components_F1(self):
        input_dict = {'1q_components': [1, 1], 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_1q_components_P(self):
        input_dict = {'1q_components': ["x", "y"], 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_1q_indices_F1(self):
        input_dict = {'1q_indices': [1, 1], 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_1q_indices_F2(self):
        input_dict = {'N': 5, '1q_indices': [2, 5, 1], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_1q_indices_P(self):
        input_dict = {'N': 5, '1q_indices': [2, 4, 1], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_2q_components_F1(self):
        input_dict = {'2q_components': ["xx", "xx"], 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_2q_components_F2(self):
        input_dict = {'2q_components': "xy", 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_2q_components_P1(self):
        input_dict = {'2q_components': ["XX", "XY", "XZ", "YY", "YZ", "ZZ"], 'N': SH_N, 't_final': SH_T_FINAL,
                      'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_2q_components_P2(self):
        input_dict = {'2q_components': ["XX", "YY", "YZ", "ZZ"], 'N': SH_N, 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_2q_indices_F1(self):
        input_dict = {'N': 5, '2q_indices': [(1, 2), (3, 1), (2, 5), (3, 4)], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_2q_indices_F2(self):
        input_dict = {'N': 2, '2q_indices': [(1, 0), (2, 1), (2, 1), (0, 1), (1, 0), (2, 1), (2, 1), (0, 1)],
                      't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertNotEqual(expected, out)

    def arg_check_2q_indices_P1(self):
        input_dict = {'N': 5, '2q_indices': [(1, 2), (3, 1), (2, 4), (3, 4)], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)

    def arg_check_2q_indices_P2(self):
        input_dict = {'N': 5, '2q_indices': [(1, 2), (3, 4)], 't_final': SH_T_FINAL, 'tau': SH_TAU}
        expected = ""
        out = MPOLindbladSolver._check_argument_correctness(input_dict)
        self.assertEqual(expected, out)


def arg_check_1():
    # this check should pass (no errors)
    input_dict = {}
    input_dict['N'] = 5
    input_dict['t_final'] = 20
    input_dict['tau'] = 3
    input_dict['output_step'] = 5

    input_dict['h_x'] = 1.111
    input_dict['h_y'] = [2.222, 4, 2e-2, 777777, -0.3]
    input_dict['h_z'] = 3.333

    input_dict['J'] = [[2, 5, 6, 7, 9],
                       [4.55, -4.1, 12, -33, 10],
                       [4.55, -1.1, 17, 0, 10],
                       [4.55, -4.1, 61, -33, 10],
                       [4.55, -1.1, 11, -33, 10]]

    input_dict['J_z'] = [[2, 5, 6, 7, 9],
                         [4.55, -4.1, 12, -33, 10],
                         [4.55, -1.1, 17, 0, 10],
                         [4.55, -4.1, 61, -33, 10],
                         [4.55, -1.1, 11, -33, 10]]

    input_dict['g_0'] = [2.222, 4, 2e-2, 777777, -0.3]
    input_dict['g_1'] = np.array([1, 2, 3, 4, 5])
    input_dict['g_2'] = -4e-10
    input_dict['init_Pauli_state'] = "+x"
    input_dict['l_x'] = 5
    input_dict['l_y'] = 1
    input_dict['b_periodic_x'] = True
    input_dict['b_periodic_y'] = False
    input_dict['trotter_order'] = 3
    input_dict['max_dim'] = 100
    input_dict['max_dim_rho'] = 200
    input_dict['cut_off'] = 1e-10
    input_dict['cut_off_rho'] = 1e-11
    input_dict['b_force_rho_trace'] = False
    input_dict['b_force_rho_hermitian'] = True
    input_dict['save_state_file'] = "C:\\output_of_my_simulation"
    input_dict['1q_components'] = ["x", "y", "z"]
    input_dict['1q_indices'] = [1, 3, 4]
    input_dict['2q_components'] = ["XX", "XY", "XZ", "YY", "YZ", "ZZ"]
    input_dict['2q_indices'] = [(1, 2), (3, 1), (2, 4), (3, 4)]

    out = MPOLindbladSolver._check_argument_correctness(input_dict)
    if out == "":
        print("Check 1 Passed")
    else:
        print("Check 1 Failed")
        print('output:\n' + out)


def arg_check_2():
    input_dict = {}
    input_dict['N'] = 5
    input_dict['t_final'] = -9  # should fail
    input_dict['tau'] = 0.1

    input_dict['h_x'] = 1.111
    input_dict['h_y'] = [2.222, 4, 2e-2, 777777, -0.3]
    input_dict['h_z'] = 3.333

    input_dict['J_z'] = [[2, 5, 6, 7, 9],
                         [4.55, -4.1, 12, -33, 10],
                         [4.55, -1.1, 17, 0],
                         [4.55, -4.1, 61, -33, 10],
                         [4.55, -1.1, 11, -33, 10]]  # this should fail

    input_dict['J'] = [[2, 5, 6, 7, 9],
                       [4.55, -4.1, 11, -33, 11e-9],
                       [4.55, -2.1, 11, 0, 10],
                       [6.25, -3.1, 2e-5, -33, 10]]  # this should fail

    input_dict['g_0'] = [2.222, 4, 777777, -0.3]  # this should fail
    input_dict['g_1'] = -99
    input_dict['g_2'] = "aaa"  # this should fail
    input_dict['init_Pauli_state'] = "-z"
    #    input_dict['l_x'] =
    #    input_dict['l_y'] =
    input_dict['b_periodic_x'] = 0  # this should fail
    input_dict['b_periodic_y'] = 1  # this should fail
    input_dict['trotter_order'] = 3
    input_dict['max_dim'] = 100
    input_dict['max_dim_rho'] = 200
    input_dict['cut_off'] = 1e-10
    input_dict['cut_off_rho'] = 1e-11
    input_dict['b_force_rho_trace'] = "False"  # this should fail
    input_dict['b_force_rho_hermitian'] = True
    input_dict['output_step'] = 0.6  # this should fail
    input_dict['save_state_file'] = "C:\\output_of_my_simulation"
    input_dict['1q_components'] = ["x", "y", "j"]  # this should fail
    input_dict['1q_indices'] = [1, 3, 5]
    input_dict['2q_components'] = ["XX", "XY", "A", "YY", "YZ", "ZZ"]  # this should fail
    input_dict['2q_indices'] = [(1, 2), (3, 5, 4), (2, 4)]  # this should fail

    out = MPOLindbladSolver._check_argument_correctness(input_dict)
    if out.count("Error") == 13:
        print("Check 2 Passed")
    else:
        print("Check 2 Failed")
        print('output:\n' + out)


def arg_check_3():
    # in this check we should get 25 fails !
    input_dict = {}
    input_dict['N'] = 9
    input_dict['t_final'] = "22"
    input_dict['tau'] = "aaa"

    input_dict['h_x'] = "aa1.111"
    input_dict['h_y'] = "[2.222,       4,   2e-2, 777777,   -0.3]"
    input_dict['h_z'] = "aa3.333"

    input_dict['J_z'] = [[2, 5, 6, '7', 9],
                         [4.55, -4.1, 12, -33, 10],
                         [4.55, -1.1, 17, 0],
                         [4.55, -4.1, 61, -33, 10],
                         [4.55, -1.1, 11, -33, 10]]

    input_dict['J'] = [[2, 5, '6', 7, 9],
                       [4.55, -4.1, 11, -33, 11e-9],
                       [4.55, -2.1, 11, 0, 10],
                       [6.25, -3.1, 2e-5, -33, 10]]

    input_dict['g_0'] = [2.222, 4]
    input_dict['g_1'] = (-11, 22)
    input_dict['g_2'] = "aaa"
    input_dict['init_Pauli_state'] = "+a2"

    input_dict['b_periodic_x'] = 0
    input_dict['b_periodic_y'] = 1
    input_dict['trotter_order'] = (3.99, 99)
    input_dict['max_dim'] = 100.99
    input_dict['max_dim_rho'] = 200.99
    input_dict['cut_off'] = "1e-10"
    input_dict['cut_off_rho'] = "1e-11"
    input_dict['b_force_rho_trace'] = "False"
    input_dict['b_force_rho_hermitian'] = 222
    input_dict['output_step'] = 0.6
    input_dict['save_state_file'] = "C:\\output_of_my_simulation"
    input_dict['1q_components'] = ["x", "y", "j"]
    input_dict['1q_indices'] = [1, 3, 1, 5, 1]
    input_dict['2q_components'] = ["XX", "XY", "A", "YY", "YZ", "ZZ"]
    input_dict['2q_indices'] = [(1, 2), (3, 5, 4), (2, 4)]

    out = MPOLindbladSolver._check_argument_correctness(input_dict)
    if out.count("Error") == 25:
        print("Check 3 Passed")
    else:
        print("Check 3 Failed")
        print('output:\n' + out)


def arg_check_4():
    # this check should pass (no errors)
    input_dict = {}
    input_dict['N'] = 5
    input_dict['t_final'] = 20
    input_dict['tau'] = 0.1

    input_dict['h_x'] = 1.111
    input_dict['h_y'] = [2.222, 4, 2e-2, 777777, -0.3]
    input_dict['h_z'] = 3.333

    input_dict['J_z'] = [[2, 5, 6, 7, 9],
                         [4.55, -4.1, 12, -33, 10],
                         [4.55, -1.1, 17, 0, 10],
                         [4.55, -4.1, 61, -33, 10],
                         [4.55, -1.1, 11, -33, 10]]

    input_dict['J'] = [[2, 5, 6, 7, 9],
                       [4.55, -4.1, 11, -33, 11e-9],
                       [4.55, -2.1, 11, 0, 10],
                       [6.25, -3.1, 2e-5, -33, 10],
                       [4.15, -4.1, 11, -33, 11]]

    input_dict['g_0'] = [2.222, 4, 2e-2, 777777, -0.3]
    input_dict['g_1'] = -99
    input_dict['g_2'] = -4e-10
    input_dict['init_Pauli_state'] = "-y"
    input_dict['l_x'] = 1
    input_dict['l_y'] = 5
    input_dict['b_periodic_x'] = True
    input_dict['b_periodic_y'] = False
    input_dict['trotter_order'] = 3
    input_dict['max_dim'] = 100
    input_dict['max_dim_rho'] = 200
    input_dict['cut_off'] = 1e-10
    input_dict['cut_off_rho'] = 1e-11
    input_dict['b_force_rho_trace'] = False
    input_dict['b_force_rho_hermitian'] = True
    input_dict['output_step'] = 1
    input_dict['save_state_file'] = "C:\\output_of_my_simulation"
    input_dict['1q_components'] = ["x", "y", "z"]
    input_dict['1q_indices'] = [1, 3, 2]
    input_dict['2q_components'] = ["XX", "XY", "XZ", "YY", "YZ", "ZZ"]
    input_dict['2q_indices'] = [(1, 2), (3, 2), (2, 4)]

    out = MPOLindbladSolver._check_argument_correctness(input_dict)
    if out == "":
        print("Check 4 Passed")
    else:
        print("Check 4 Failed")
        print('output:\n', out)


def arg_check_5():
    input_dict = {}
    input_dict['N'] = 5
    input_dict['t_final'] = 20
    input_dict['tau'] = 0.1

    input_dict['h_x'] = 1.111
    input_dict['h_y'] = [2.222, 4, 2e-2, 777777, -0.3]
    input_dict['h_z'] = 3.333

    input_dict['J_z'] = [[2, 5, 6, 7, 9],
                         [4.55, -4.1, 12, -33, 10],
                         [4.55, -1.1, 17, 0, 10],
                         [4.55, -4.1, 61, -33, 10],
                         [4.55, -1.1, 11, -33, 10]]

    input_dict['J'] = [[2, 5, 6, 7, 9],
                       [4.55, -4.1, 11, -33, 11e-9],
                       [4.55, -2.1, 11, 0, 10],
                       [6.25, -3.1, 2e-5, -33, 10],
                       [4.15, -4.1, 11, -33, 11]]

    input_dict['g_0'] = [2.222, 4, 2e-2, 777777, -0.3]
    input_dict['g_1'] = -99
    input_dict['g_2'] = -4e-10
    input_dict['init_Pauli_state'] = "-x"
    #    input_dict['l_x'] =
    #    input_dict['l_y'] =
    input_dict['b_periodic_x'] = True
    input_dict['b_periodic_y'] = False
    input_dict['trotter_order'] = 3
    input_dict['max_dim'] = 100
    input_dict['max_dim_rho'] = 200
    input_dict['cut_off'] = 1e-10
    input_dict['cut_off_rho'] = 1e-11
    input_dict['b_force_rho_trace'] = False
    input_dict['b_force_rho_hermitian'] = True
    input_dict['output_step'] = 1
    input_dict['save_state_file'] = "C:\\output_of_my_simulation"
    input_dict['1q_components'] = ["x", "y", "z"]
    input_dict['1q_indices'] = [1, 3, 99]
    input_dict['2q_components'] = ["XX", "XY", "XZ", "YY", "YZ", "ZZ"]
    input_dict['2q_indices'] = [(1, 2), (3, 1), (2, 4), (3, 4)]
    try:
        MPOLindbladSolver.build_input_file(input_dict)
        print("Check 5 Failed, expected to get an exception\n")
    except:
        print("Check 5 Passed\n")


def arg_check_6():
    input_dict = {}
    input_dict['N'] = 5
    input_dict['t_final'] = 20
    input_dict['tau'] = 0.1

    input_dict['h_x'] = 1.111
    input_dict['h_y'] = [2.222, 4, 2e-2, 777777, -0.3]
    input_dict['h_z'] = 3.333

    input_dict['J_z'] = [[2, 5, 6, 7, 9],
                         [4.55, -4.1, 12, -33, 10],
                         [4.55, -1.1, 17, 0, 10],
                         [4.55, -4.1, 61, -33, 10],
                         [4.55, -1.1, 11, -33, 10]]

    input_dict['J'] = [[2, 5, 6, 7, 9],
                       [4.55, -4.1, 11, -33, 11e-9],
                       [4.55, -2.1, 11, 0, 10],
                       [6.25, -3.1, 2e-5, -33, 10],
                       [4.15, -4.1, 11, -33, 11]]

    input_dict['g_0'] = [2.222, 4, 2e-2, 777777, -0.3]
    input_dict['g_1'] = -99
    input_dict['g_2'] = -4e-10
    input_dict['init_Pauli_state'] = "+z"
    #    input_dict['l_x'] =
    #    input_dict['l_y'] =
    input_dict['b_periodic_x'] = True
    input_dict['b_periodic_y'] = False
    input_dict['trotter_order'] = 3
    input_dict['max_dim'] = 100
    input_dict['max_dim_rho'] = 200
    input_dict['cut_off'] = 1e-10
    input_dict['cut_off_rho'] = 1e-11
    input_dict['b_force_rho_trace'] = False
    input_dict['b_force_rho_hermitian'] = True
    input_dict['output_step'] = 1
    input_dict['save_state_file'] = "C:\\output_of_my_simulation"
    input_dict['1q_components'] = ["x", "y", "z"]
    input_dict['1q_indices'] = [1, 2, 4]
    input_dict['2q_components'] = ["XX", "XY", "XZ", "YY", "YZ", "ZZ"]
    input_dict['2q_indices'] = [(1, 2), (3, 1), (2, 4), (3, 4)]
    try:
        MPOLindbladSolver.build_input_file(input_dict)
        print("Check 6 Passed\n")
    except:
        print("Check 6 Failed, exception was not expected\n")


#
#   def second_check():
#       input_dict = {}
#       input_dict['N'] =
#       input_dict['t_final'] =
#       input_dict['tau'] =
#       input_dict['h_x'] =
#       input_dict['h_y'] =
#       input_dict['h_z'] =
#       input_dict['J_z'] =
#       input_dict['J'] =
#       input_dict['g_0'] =
#       input_dict['g_1'] =
#       input_dict['g_2'] =
#       input_dict['init_Pauli_state'] =
#       input_dict['l_x'] =
#       input_dict['l_y'] =
#       input_dict['b_periodic_x'] =
#       input_dict['b_periodic_y'] =
#       input_dict['trotter_order'] =
#       input_dict['max_dim'] =
#       input_dict['max_dim_rho'] =
#       input_dict['cut_off'] =
#       input_dict['cut_off_rho'] =
#       input_dict['b_force_rho_trace'] =
#       input_dict['b_force_rho_hermitian'] =
#       input_dict['output_step'] =
#       input_dict['save_state_file'] =
#       input_dict['1q_components'] =
#       input_dict['1q_indices'] =
#       input_dict['2q_components'] =
#       input_dict['2q_indices'] =
#
#       out = MPOLindbladSolver._check_argument_correctness(input_dict)
#       print ('output:',out)
#
#   def second_check():
#       input_dict = {}
#       input_dict['N'] =
#       input_dict['t_final'] =
#       input_dict['tau'] =
#       input_dict['h_x'] =
#       input_dict['h_y'] =
#       input_dict['h_z'] =
#       input_dict['J_z'] =
#       input_dict['J'] =
#       input_dict['g_0'] =
#       input_dict['g_1'] =
#       input_dict['g_2'] =
#       input_dict['init_Pauli_state'] =
#       input_dict['l_x'] =
#       input_dict['l_y'] =
#       input_dict['b_periodic_x'] =
#       input_dict['b_periodic_y'] =
#       input_dict['trotter_order'] =
#       input_dict['max_dim'] =
#       input_dict['max_dim_rho'] =
#       input_dict['cut_off'] =
#       input_dict['cut_off_rho'] =
#       input_dict['b_force_rho_trace'] =
#       input_dict['b_force_rho_hermitian'] =
#       input_dict['output_step'] =
#       input_dict['save_state_file'] =
#       input_dict['1q_components'] =
#       input_dict['1q_indices'] =
#       input_dict['2q_components'] =
#       input_dict['2q_indices'] =
#
#       out = MPOLindbladSolver._check_argument_correctness(input_dict)
#       print ('output:',out)
#

arg_check_1()
arg_check_2()
arg_check_3()
arg_check_4()
arg_check_5()
arg_check_6()
