#ifndef _SIMULATIONPARAMETERS_
#define _SIMULATIONPARAMETERS_

using namespace itensor;
using namespace std;

//____________________________________________________________________
class SimulationParameters : public Parameters
{
public:
    SimulationParameters() //constructor
    {
        // The parameters below concern the simulation algorithm and approximations, and are not
        // model-specific (model-specific parameters should be defined in ModelParameters.h).

        operator[]("t_init") = "0";         // Initial time.
        operator[]("t_final") = "1";        // Final time.
        operator[]("tau") = "0.1";          // Step for the time evolution (should be smaller than
            // typical oscillation periods in the dynamics, but not too small for good performance)
        operator[]("output_step") = "1";    // Determines every how many tau time steps to compute
            // (and save) the observables. If set to 0, no observables are computed.

        operator[]("trotter_order") = "4";  // Possible choices are 2, 3, 4. 3 or 4 are recommended.
        operator[]("max_dim_rho") = "400";  // Maximum bond dimension for density matrices
        operator[]("cut_off_rho") = "1e-16"; // Maximum truncation error for density matrices. The actual
        	// truncation is done using the most severe condition between cut_off_rho and max_dim_rho.

        operator[]("b_force_rho_trace") = "1";		// Whether to force the density matrix trace to 1,
            // by substituting rho /= trace{rho} at every time step, compensating for finite-step errors
        operator[]("force_rho_hermitian_step") = "4";	// Determines every how many tau time steps
        	// to substitute rho = 0.5 * (rho + rho^dagger). This may reduce certain errors, but is
        	// computationally expensive.
        operator[]("b_initial_rho_compression") = "0";	// If nonzero, after reading rho from
         	// a saved file, perform a re-gauging/compression using iTensor's method orthogonalize().

        operator[]("init_pauli_state") = "+z";  // Initialize a Pauli state. Can be specified for
        	// every qubit separately (as a comma-separated list), or uniformly for all qubits.
        	// The string format is + or - in the first character, and x, y, z in the second
        	// character, denoting a single-qubit state pointing along the positive/negative
        	// direction of the specified axis of the Bloch sphere.
        	// If the string is not of this format, it is attempted to be parsed as floating point
        	// number that defines a diagonal mixed, giving the probability of the |up> state.
        operator[]("init_graph_state") = "";  // Initialize a graph state. A list of qubit indexes
        	// is expected with all pairs on which a CZ gate is applied (after starting with all qubits
        	// along the +x axis).
        operator[]("load_files_prefix") = "";	// If not an empty string, the initial state
         	// (density matrix rho) is to be read from the file system. Three files are being used,
         	// with names appended with ".state.ops", ".state.sites" and ".state.rho".
        operator[]("b_save_final_state") = "0";	// Whether to save the final state (density matrix) to
        	// the file system. Three files are generated, with the files names starting with the
        	// `output_files_prefix` string, with the endings ".state.rho", ".state.sites", and ".state.ops".
                                              
        operator[]("unique_id") = ""; // An optional unique id identifying the simulation. Not currently used (except for being saved in the input and log files).
        operator[]("metadata") = ""; // An optional user information, ignored by the solver (except for being saved in the input and log files).
        operator[]("input_file") = ""; // If not empty => name of the file from which some parameters must be read (in addition to the command line ones).
        operator[]("output_files_prefix") = "lindblad"; // Path and prefix of the file names where various simulation output is written

    }
};

        //OLD initial state settings
/*        operator[]("x_init") = "0";    //Initial state = spins pointing in the x direction
        operator[]("y_init") = "0";    //Initial state = spins pointing in the y direction
        operator[]("xm_init") = "0";    //Initial state = spins pointing in the -x direction
        operator[]("ym_init") = "0";    //Initial state = spins pointing in the -y direction
        operator[]("up_init") = "1";   //Set to "1" if you want to start from a (pure) state where all the spins are "up"
        operator[]("down_init") = "0"; //Set to "1" if you want to start from a (pure) state where all the spins are "up"
        operator[]("rho_inf_init") = "0";     //Set to "1" if you want to start from rho=identity (infinite temperature density matrix)

        operator[]("max_dim_psi") = "500";     //maximum bond dimension for wave-functions
        operator[]("cut_off_psi") = "1e-9";    //maximum truncation error  for wave-functions
        operator[]("sweeps") = "0";     //maximum number of sweeps in the DMRG (to get the initial wave-function as the ground-state of H0)
        operator[]("energy") = "1e-12"; //convergence criterium on the energy. This is only used in the initial DMRG runs to coinstruct (if needed) the initial state as the ground state of H0.

        operator[]("dmrgLDL") = "0";     //Set to "1" if you want to do some DMRG sweeps to minimize Ldagger*L (L:Lindbladian), to get (or approach) the steady state
        operator[]("LDLconv") = "5e-4";  //convergence criterium on L^dagger * L -- this is a relative value, so the DMRG stops when |dE/E|< LDLconv. In an exact calculation of the steady state E=0
        operator[]("sweepsRho") = "999"; //maximum number of sweeps in the DMRG (to get the initial density matrix as the ground-state of L^dagger*L)
        //If not equal to "" the initial state is a pure state (wavefunction) that will be read from the disk.
        operator[]("load_purestate_file") = "";
        //If not equal to "" the initial state is a pure state (wavefunction) that will be read from the disk.
        operator[]("save_purestate_file") = "";
*/
//____________________________________________________________________
#endif
