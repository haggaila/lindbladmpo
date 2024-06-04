// Licensed under the Apache License, Version 2.0 (the "License"); you may
// not use this file except in compliance with the License. You may obtain
// a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations
// under the License.

#ifndef _MPS_MPO_UTILS_
#define _MPS_MPO_UTILS_
#include "io_utils.h"
#include "itensor/all.h"
#include <map>
#include <string>
#include <vector>
using namespace itensor;
using namespace std;
//____________________________________________________________

class MyDMRGObserver : public DMRGObserver
{
    double previous_energy;
    const double precision;
    bool relative; // false => stop criterium on |E_n - E_{n-1} |, true => criterium on |E_n - E_{n-1} |/|E_n|
  public:
    MyDMRGObserver(const MPS &psi, double prec = 1e-10, bool rel = false)
        : DMRGObserver(psi), precision(prec), relative(rel)
    {
    }

    bool checkDone(const Args &args = Args::global())
    {
        const double energy = args.getReal("Energy", 0);
        cout2 << "    Change in <L^+ L>: " << energy - previous_energy
              << "\trelative change: " << (energy - previous_energy) / (abs(previous_energy) + 1e-15) << "\n";
        if (relative)
        {
            if (abs(energy - previous_energy) / (abs(previous_energy) + 1e-15) < precision)
            {
                cout2 << "   <L^+ L> has converged (relative change <" << precision << ") => stop the DMRG.\n";
                return true;
            }
            else
            {
                previous_energy = energy;
                return false;
            }
        }
        else
        {
            if (abs(energy - previous_energy) < precision)
            {
                cout2 << "   Energy has converged (change <" << precision << ") => stop the DMRG.\n";
                return true;
            }
            else
            {
                previous_energy = energy;
                return false;
            }
        }
    }
};
//_____________________________________________________
inline Cplx PureStateObs(const string &opname, MPS psi, int i, const SiteSet &sites) //<psi|O|psi> at some site i
{
    // Note that these are iTensor spin operators (i.e., half Paulis for x,y,z)
    auto O = op(sites, opname, i);
    psi.position(i);
    ITensor A = psi.A(i);
    ITensor A_ = dag(prime(psi.A(i), "Site"));
    A *= O;
    ITensor B = A * A_;
    return B.cplx();
}
//____________________________________________________________________

inline int BondDim(const MPS &psi, int i)
{
    auto bond_index = commonIndex(psi.A(i), psi.A(i + 1), "Link");
    return (bond_index.dim());
}
inline int BondDim(const MPO &H, int i)
{
    auto bond_index = commonIndex(H.A(i), H.A(i + 1), "Link");
    return (bond_index.dim());
}
//____________________________________________________________________
double Entropy(MPS psi, int i, int local_space_dim = 0); // returns the von Neumann entropy on some bond (i,i+1)
//____________________________________________________________________
double OSEE(MPS rho, int i);
void prints_SVD_spectrum(ostream &o, MPS psi, int i);
//____________________________________________________________________
#endif
