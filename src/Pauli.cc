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

#include "Pauli.h"
#include "io_utils.h"
#include "mps_mpo_utils.h"
#include "itensor/all.h"
#include <string>
#include <chrono>

using namespace std::chrono;

PauliSite::PauliSite() {}
PauliSite::PauliSite(Index I) : s(I) {}

PauliSite::PauliSite(Args const &args)
{
  auto ts = TagSet("Site,PSite");
  if (args.defined("SiteNumber"))
    ts.addTags("n=" + str(args.getInt("SiteNumber")));
  s = Index(4, ts);
}
Index PauliSite::index() const { return s; }

//__________________________________________
IndexVal PauliSite::state(string const &state) const
{
  if (state == "uu")
  {
    return s(1);
  }
  else if (state == "du")
  {
    return s(2);
  }
  else if (state == "ud")
  {
    return s(3);
  }
  else if (state == "dd")
  {
    return s(4);
  }
  else
  {
    Error("State " + state + " not recognized");
  }
  return IndexVal();
}
//__________________________________________
ITensor PauliSite::op(const string &opname, const Args &args) const
{
  auto sP = prime(s);

  auto uu = s(1), dd = s(4), du = s(2), ud = s(3);
  auto uu_ = sP(1), dd_ = sP(4), du_ = sP(2), ud_ = sP(3);

  // Note: dag(...) returns a copy of the Index, with its arrow direction reversed.
  auto Op = ITensor(dag(s), sP);
  // About the notations below:
  // no "_" prefix in the operator name indicates that the operator acts on the right of the density matrix
  // A prefix "_" indicate that the operator acts on the left of the density matrix
  if (opname == "Sz")
  {
    Op.set(dd_, dd, -1.0);
    Op.set(du_, du, +1.0);
    Op.set(ud_, ud, -1.0);
    Op.set(uu_, uu, +1.0);
  }
  else if (opname == "S+")
  {
    Op.set(ud_, uu, 1.0);
    Op.set(dd_, du, 1.0);
  }
  else if (opname == "S-")
  {
    Op.set(du_, dd, 1.0);
    Op.set(uu_, ud, 1.0);
  }
  else if (opname == "Sx")
  {
    Op.set(ud_, uu, 1.0);
    Op.set(dd_, du, 1.0);
    Op.set(du_, dd, 1.0);
    Op.set(uu_, ud, 1.0);
  }
  else if (opname == "Sy")
  {
    Op = ITensor(s, sP);
    Op.set(ud_, uu, -Cplx_i);
    Op.set(dd_, du, -Cplx_i);
    Op.set(du_, dd, Cplx_i);
    Op.set(uu_, ud, Cplx_i);
  }
  else if (opname == "_Sz")
  {
    Op.set(dd, dd_, -1.0);
    Op.set(du, du_, -1.0);
    Op.set(ud, ud_, +1.0);
    Op.set(uu, uu_, +1.0);
  }
  else if (opname == "_S+")
  {
    Op.set(dd, ud_, 1.0);
    Op.set(du, uu_, 1.0);
  }
  else if (opname == "_S-")
  {
    Op.set(uu, du_, 1.0);
    Op.set(ud, dd_, 1.0);
  }
  else if (opname == "_Sx")
  {
    Op = ITensor(s, sP);
    Op.set(dd, ud_, 1.0);
    Op.set(du, uu_, 1.0);
    Op.set(uu, du_, 1.0);
    Op.set(ud, dd_, 1.0);
  }
  else if (opname == "_Sy")
  {
    Op = ITensor(s, sP);
    Op.set(dd, ud_, -Cplx_i);
    Op.set(du, uu_, -Cplx_i);
    Op.set(uu, du_, Cplx_i);
    Op.set(ud, dd_, Cplx_i);
  }
  else if (opname == "Sz_Sz")
  {
    Op.set(dd_, dd, +1.0);
    Op.set(du_, du, -1.0);
    Op.set(ud_, ud, -1.0);
    Op.set(uu_, uu, +1.0);
  }
  else if (opname == "Sx_Sx")
  {
    Error("Operator " + opname + " missing implementation.");
  }
  else if (opname == "_S-S+")
  {
    Op.set(dd_, uu, 1.0);
  }
  else if (opname == "_S+S-")
  {
    Op.set(uu_, dd, 1.0);
  }
  else if (opname == "projUp" || opname == "Su")
  {
    Op.set(uu_, uu, 1.0);
    Op.set(du_, du, 1.0);
  }
  else if (opname == "projDn" || opname == "Sd")
  {
    Op.set(ud_, ud, 1.0);
    Op.set(dd_, dd, 1.0);
  }
  else if (opname == "_projUp")
  {
    Op.set(uu_, uu, 1.0);
    Op.set(ud_, ud, 1.0);
  }
  else if (opname == "_projDn")
  {
    Op.set(dd_, dd, 1.0);
    Op.set(du_, du, 1.0);
  }
  else if (opname == "SqrtX")
  {
    //SqrtX = 0.5*[ (1+i)*Id + (1-i)*Sx ]
    Op.set(dd_, dd, 0.5*(1.+Cplx_i));
    Op.set(du_, du, 0.5*(1.+Cplx_i));
    Op.set(ud_, ud, 0.5*(1.+Cplx_i));
    Op.set(uu_, uu, 0.5*(1.+Cplx_i));

    Op.set(ud_, uu, 0.5*(1.-Cplx_i));
    Op.set(dd_, du, 0.5*(1.-Cplx_i));
    Op.set(du_, dd, 0.5*(1.-Cplx_i));
    Op.set(uu_, ud, 0.5*(1.-Cplx_i));

  }
  else if (opname == "_SqrtX")
  {
    Op.set(dd_, dd, 0.5*(1.-Cplx_i));
    Op.set(du_, du, 0.5*(1.-Cplx_i));
    Op.set(ud_, ud, 0.5*(1.-Cplx_i));
    Op.set(uu_, uu, 0.5*(1.-Cplx_i));
    
    Op.set(dd, ud_, 0.5*(1.+Cplx_i));
    Op.set(du, uu_, 0.5*(1.+Cplx_i));
    Op.set(uu, du_, 0.5*(1.+Cplx_i));
    Op.set(ud, dd_, 0.5*(1.+Cplx_i)); 
  }
  else if (opname == "H")
  {
    //Hadamard gate
    //H = sqrt(0.5)*[ Sx + Sz ]
    const double sqrt05 = pow(.5, .5);
    Op.set(ud_, uu, sqrt05);
    Op.set(dd_, du, sqrt05);
    Op.set(du_, dd, sqrt05);
    Op.set(uu_, ud, sqrt05);
    Op.set(dd_, dd, -sqrt05);
    Op.set(du_, du, +sqrt05);
    Op.set(ud_, ud, -sqrt05);
    Op.set(uu_, uu, +sqrt05);

  }
  else if (opname == "_H")
  {
    const double sqrt05 = pow(.5, .5);
    Op.set(dd, dd_, -sqrt05);
    Op.set(du, du_, -sqrt05);
    Op.set(ud, ud_, sqrt05);
    Op.set(uu, uu_, sqrt05);
    Op.set(dd, ud_, sqrt05);
    Op.set(du, uu_, sqrt05);
    Op.set(uu, du_, sqrt05);
    Op.set(ud, dd_, sqrt05);
  }
  else if (opname == "Id")
  {
    Op.set(dd_, dd, 1.0);
    Op.set(du_, du, 1.0);
    Op.set(ud_, ud, 1.0);
    Op.set(uu_, uu, 1.0);
  }
  else
  {
    Error("Operator " + opname + " name not recognized.");
  }
  return Op;
}
//____________________________________________________________________
//Trace of rho
complex<double> SpinHalfSystem::trace_rho() const
{
  return innerC(Identity, rho);
}

complex<double> SpinHalfSystem::trace_rho2() const
{
  return innerC(rho, rho);
}

//Constructor
SpinHalfSystem::SpinHalfSystem(int size) : N(size),
                                           sites(N, {"ConserveQNs=", false}),
                                           siteops(N), rho(siteops),
                                           Lindbladian(siteops)
{
}
void SpinHalfSystem::ConstructIdentity()
{
  //Initialize the diagonal density operator
  //In case we read data from disk, this must be called
  //after the 'sites' are defined (read from disk)
  Identity = MPS(InitState(siteops, "dd"));
  ITensor &U1 = Identity.ref(1);
  if (N > 1)
  {
    Index a = commonIndex(U1, Identity.A(2));
    Index p = siteops(1);
    U1.set(IndexVal(p, 1), IndexVal(a, 1), 1.0);
    U1.set(IndexVal(p, 4), IndexVal(a, 1), 1.0);

    ITensor &UN = Identity.ref(N);
    p = siteops(N);
    a = commonIndex(UN, Identity.A(N - 1));
    UN.set(IndexVal(p, 1), IndexVal(a, 1), 1.0);
    UN.set(IndexVal(p, 4), IndexVal(a, 1), 1.0);

    for (int j = 2; j <= N - 1; ++j)
    {
      ITensor &U = Identity.ref(j);
      Index a = commonIndex(U, Identity.A(j + 1));
      Index b = commonIndex(U, Identity.A(j - 1));
      Index p = siteops(j);
      U.set(IndexVal(p, 1), IndexVal(a, 1), IndexVal(b, 1), 1.0);
      U.set(IndexVal(p, 4), IndexVal(a, 1), IndexVal(b, 1), 1.0);
    }
  }
  else
  {
    //N=1, single site system (but not supported by iTensor)
    Index p = siteops(1);
    U1.set(IndexVal(p, 1), 1.0);
    U1.set(IndexVal(p, 4), 1.0);
  } 
}

//Convert a pure state (psi) of the chain into a density matrix rho=|psi><psi| (projector onto psi)
void SpinHalfSystem::psi2rho(const MPS &psi, MPS&RHO,const Args &args)
{
  ITensor right_combined, left_combined;
  int N=psi.length();
  if (RHO.length()!=N) cout2<<"Error in psi2rho: psi has lenght "<<N<<" and RHO has lenghth "<<RHO.length()<<"\n.",exit(0);
  
  for (int j = 1; j <= N; ++j)
  {
    ITensor A = psi(j);
    ITensor A_ = prime(psi(j));
    A_.conj();
    ITensor V = A * A_;

    Index new_left, new_right, new_right_tagged, new_left_tagged;
    if (j > 1)
    {                                 //Not the first site
      left_combined = right_combined; //Take the right_(...) of the previous site
      V *= left_combined;
      //New bond index
      new_left = commonIndex(left_combined, V);
      new_left_tagged = removeTags(new_left, "CMB");
      new_left_tagged.addTags(string("l=") + to_string(j - 1));
    }
    if (j < N)
    { //Not the last site
      const ITensor &Anext(psi(j + 1));
      ITensor Anext_ = prime(psi(j + 1));
      Index right = commonIndex(A, Anext, "Link");
      Index right_ = commonIndex(A_, Anext_, "Link");
      tie(right_combined, new_right) = combiner(right, right_);
      V *= right_combined;
      new_right_tagged = removeTags(new_right, "CMB");
      new_right_tagged.addTags(string("l=") + to_string(j));
    }

    Index spin = findIndex(A, "Site");   //iTensor v3
    Index spin_ = findIndex(A_, "Site"); //iTensor v3
    Index J = siteops(j);                // J takes 4 values
    ITensor &R = RHO.ref(j);
    if (j == 1)
    {
      R = ITensor(J, new_right_tagged);
    }
    else
    {
      if (j == N)
      {
        R = ITensor(J, new_left_tagged);
      }
      else
      { //Middle of the chain
        R = ITensor(J, new_right_tagged, new_left_tagged);
      }
    }
    //Loop on the physical index (dimension 4=2*2)
    for (int i1 = 1; i1 <= 2; i1++)
    {
      const IndexVal i1_(spin, i1);
      for (int i2 = 1; i2 <= 2; i2++)
      {
        const IndexVal i2_(spin_, i2);
        const int i = (i2 - 1) * 2 + i1; // this guy runs from 1 (uu) to 4 (dd)
        const IndexVal J_(J, i);         //Value 'i' assigned to the index J
        if (j == 1)
        {
          const int bdim_right = new_right.dim();
          for (int a = 1; a <= bdim_right; a++)
          {
            const IndexVal new_right_(new_right, a);
            const IndexVal new_right_tagged_(new_right_tagged, a);
            complex<double> v = V.cplx(i1_, i2_, new_right_);
            R.set(J_, new_right_tagged_, v);
          }
        }
        else
        {
          if (j == N)
          {
            const int bdim_left = new_left.dim();
            for (int b = 1; b <= bdim_left; b++)
            {
              const IndexVal new_left_(new_left, b);
              const IndexVal new_left_tagged_(new_left_tagged, b);
              R.set(J_, new_left_tagged_, V.cplx(i1_, i2_, new_left_));
            }
          }
          else
          { //Middle of the chain => do left & right loops
            const int bdim_right = new_right.dim();
            const int bdim_left = new_left.dim();
            //Write one element of R, to allocate the memory for this tensor:
            //const IndexVal new_right_(new_right, 1);
            //const IndexVal new_left_(new_left, 1);
            //const IndexVal new_right_tagged_(new_right_tagged, 1);
            //const IndexVal new_left_tagged_(new_left_tagged, 1);
            //R.set(J_,new_left_tagged_, new_right_tagged_,V.cplx(i1_,i2_,new_left_,new_right_));
            // note: if we omit the line above, the parallel loop below
            //would fail (segmentation fault) because several threads
            //would independently attempt to allocate the tensor R

            //Fill this (potentially big) tensor R using a parallelized loop:
            //#pragma omp parallel for
            for (int a = 1; a <= bdim_right; a++)
            {
              const IndexVal new_right_(new_right, a);
              const IndexVal new_right_tagged_(new_right_tagged, a);
              for (int b = 1; b <= bdim_left; b++)
              {
                const IndexVal new_left_(new_left, b);
                const IndexVal new_left_tagged_(new_left_tagged, b);
                R.set(J_, new_left_tagged_, new_right_tagged_, V.cplx(i1_, i2_, new_left_, new_right_));
              }
            }
          }
        }
      }
    }
  }
}

void SpinHalfSystem::psi2rho(const MPS &psi, const Args &args) {
  psi2rho(psi, rho,args);
}


/*
//Convert a pure state (psi) of the chain into the density matrix of the system (projector |psi><psi|)
void SpinHalfSystem::psi2rho(const MPS &psi, const Args &args)
{
  cout2 << "Norm of |psi>: (<psi|psi>)^(1/2)=" << norm(psi) << "\n";
  cout2 << "Constructing rho from |psi> (exactly)...";
  cout2.flush();

  ITensor right_combined, left_combined;

  for (int j = 1; j <= N; ++j)
  {
    ITensor A = psi(j);
    ITensor A_ = prime(psi(j));
    A_.conj();
    ITensor V = A * A_;

    Index new_left, new_right, new_right_tagged, new_left_tagged;
    if (j > 1)
    {                                 //Not the first site
      left_combined = right_combined; //Take the right_(...) of the previous site
      V *= left_combined;
      //New bond index
      new_left = commonIndex(left_combined, V);
      new_left_tagged = removeTags(new_left, "CMB");
      new_left_tagged.addTags(string("l=") + to_string(j - 1));
    }
    if (j < N)
    { //Not the last site
      const ITensor &Anext(psi(j + 1));
      ITensor Anext_ = prime(psi(j + 1));
      Index right = commonIndex(A, Anext, "Link");
      Index right_ = commonIndex(A_, Anext_, "Link");
      // v3:
      tie(right_combined, new_right) = combiner(right, right_);
      V *= right_combined;
      new_right_tagged = removeTags(new_right, "CMB");
      new_right_tagged.addTags(string("l=") + to_string(j));
    }

    Index spin = findIndex(A, "Site");   //iTensor v3
    Index spin_ = findIndex(A_, "Site"); //iTensor v3
    Index J = siteops(j);                // J takes 4 values
    ITensor &R = rho.ref(j);
    if (j == 1)
    {
      R = ITensor(J, new_right_tagged);
    }
    else
    {
      if (j == N)
      {
        R = ITensor(J, new_left_tagged);
      }
      else
      { //Middle of the chain
        R = ITensor(J, new_right_tagged, new_left_tagged);
      }
    }
    //Loop on the physical index (dimension 4=2*2)
    for (int i1 = 1; i1 <= 2; i1++)
    {
      const IndexVal i1_(spin, i1);
      for (int i2 = 1; i2 <= 2; i2++)
      {
        const IndexVal i2_(spin_, i2);
        const int i = (i2 - 1) * 2 + i1; // this guy runs from 1 (uu) to 4 (dd)
        const IndexVal J_(J, i);         //Value 'i' assigned to the index J
        if (j == 1)
        {
          const int bdim_right = new_right.dim();
          for (int a = 1; a <= bdim_right; a++)
          {
            const IndexVal new_right_(new_right, a);
            const IndexVal new_right_tagged_(new_right_tagged, a);
            complex<double> v = V.cplx(i1_, i2_, new_right_);
            R.set(J_, new_right_tagged_, v);
          }
        }
        else
        {
          if (j == N)
          {
            const int bdim_left = new_left.dim();
            for (int b = 1; b <= bdim_left; b++)
            {
              const IndexVal new_left_(new_left, b);
              const IndexVal new_left_tagged_(new_left_tagged, b);
              R.set(J_, new_left_tagged_, V.cplx(i1_, i2_, new_left_));
            }
          }
          else
          { //Middle of the chain => do left & right loops
            const int bdim_right = new_right.dim();
            const int bdim_left = new_left.dim();
            //Write one element of R, to allocate the memory for this tensor:
            //const IndexVal new_right_(new_right, 1);
            //const IndexVal new_left_(new_left, 1);
            //const IndexVal new_right_tagged_(new_right_tagged, 1);
            //const IndexVal new_left_tagged_(new_left_tagged, 1);
            //R.set(J_,new_left_tagged_, new_right_tagged_,V.cplx(i1_,i2_,new_left_,new_right_));
            // note: if we omit the line above, the parallel loop below
            //would fail (segmentation fault) because several threads
            //would independently attempt to allocate the tensor R

            //Fill this (potentially big) tensor R using a parallelized loop:
            //#pragma omp parallel for
            for (int a = 1; a <= bdim_right; a++)
            {
              const IndexVal new_right_(new_right, a);
              const IndexVal new_right_tagged_(new_right_tagged, a);
              for (int b = 1; b <= bdim_left; b++)
              {
                const IndexVal new_left_(new_left, b);
                const IndexVal new_left_tagged_(new_left_tagged, b);
                R.set(J_, new_left_tagged_, new_right_tagged_, V.cplx(i1_, i2_, new_left_, new_right_));
              }
            }
          }
        }
      }
    }
  }
  cout2 << "done.\n";
  cout2.flush();
  cout2 << "Max bond dimension of rho:" << maxLinkDim(rho) << "\n";
}
*/
//Expectation value of some single-site operator
Cplx SpinHalfSystem::Expect(const string &opname, int i) const
{
  MPS rho_tmp(rho); //Could we avoid making this copy ?
  const auto &Op = siteops.op(opname, i);
  rho_tmp.ref(i) *= Op;
  rho_tmp.ref(i).noPrime();
  Cplx re = innerC(Identity, rho_tmp);
  return (re);
}
//Expectation value of some two-points correlator
Cplx SpinHalfSystem::Expect(const string &opname1, int i1, const string &opname2, int i2) const
{
  MPS rho_tmp(rho); //Could we avoid making this copy ?
  const auto &Op1 = siteops.op(opname1, i1);
  rho_tmp.ref(i1) *= Op1;
  rho_tmp.ref(i1).noPrime();
  const auto &Op2 = siteops.op(opname2, i2);
  rho_tmp.ref(i2) *= Op2;
  rho_tmp.ref(i2).noPrime();
  Cplx re = innerC(Identity, rho_tmp);
  return (re);
}

//Expectation value of some three-points correlator
Cplx SpinHalfSystem::Expect(const string &opname1, int i1, const string &opname2, int i2, const string &opname3, int i3) const
{
  MPS rho_tmp(rho); //Could we avoid making this copy ?
  const auto &Op1 = siteops.op(opname1, i1);
  rho_tmp.ref(i1) *= Op1;
  rho_tmp.ref(i1).noPrime();
  const auto &Op2 = siteops.op(opname2, i2);
  rho_tmp.ref(i2) *= Op2;
  rho_tmp.ref(i2).noPrime();
  const auto &Op3 = siteops.op(opname3, i3);
  rho_tmp.ref(i3) *= Op3;
  rho_tmp.ref(i3).noPrime();

  Cplx re = innerC(Identity, rho_tmp);
  return (re);
}

Cplx SpinHalfSystem::Expect(const vector <string>& opnames, const vector <int>& indices) const
{
  if (opnames.size()!=indices.size()) cout2<<"Error in SpinHalfSystem::Expect, openames and indices should have the same size.\n",exit(1); 
  MPS rho_tmp(rho); //Could we avoid making this copy ?
  for (unsigned int n=0;n<opnames.size();n++) {
    int i=indices[n];
    const auto &Op = siteops.op(opnames[n], i);
    rho_tmp.ref(i) *= Op;
    rho_tmp.ref(i).noPrime();
  }
  Cplx re = innerC(Identity, rho_tmp);
  return (re);
}

void SpinHalfSystem::AddSingleSpinBath(double GammaPlus, double GammaMinus, double GammaDephasing,
    double GammaBitFlip, int site)
{
  if (GammaMinus)
  {
      Cplx z = GammaMinus * Cplx_i;
      Lindbladian += z, "_S-S+", site;
      Lindbladian += -z * 0.5, "_projUp", site;
      Lindbladian += -z * 0.5, "projUp", site;
  }
  if (GammaPlus)
  {
      Cplx z = GammaPlus * Cplx_i;
      Lindbladian += z, "_S+S-", site;
      Lindbladian += -z * 0.5, "_projDn", site;
      Lindbladian += -z * 0.5, "projDn", site;
  }
  if (GammaDephasing)
  {
      Cplx z = GammaDephasing * Cplx_i;
      Lindbladian += z, "Sz_Sz", site;
      Lindbladian += -z * 0.5, "Id", site;
      Lindbladian += -z * 0.5, "Id", site;
  }
  if (GammaBitFlip)
  {
      Cplx z = GammaBitFlip * Cplx_i;
      Lindbladian += z, "Sx_Sx", site;
      Lindbladian += -z * 0.5, "Id", site;
      Lindbladian += -z * 0.5, "Id", site;
  }
}
//_____________________________________________________

void SpinHalfSystem::MakeRhoHermitian(Args args)
{
	auto time_step = steady_clock::now();
	cout2 << "\tMake rho Hermitian; Max bond dimension: " << maxLinkDim(rho) << " -> ";
	cout2.flush();
	MPS rd(rho); // Copy
	// Next, take the Hermitian conjugate of rd
  for (int i = 1; i <= N; i += N - 1)
  {
    ITensor &U = rd.ref(i);
    const Index a = commonIndex(U, rd((i == 1) ? 2 : (N - 1)));
    const Index p = siteops(i);
    const IndexVal p1(p, 1), p2(p, 2), p3(p, 3), p4(p, 4);
    for (int aa = 1; aa <= a.dim(); aa++)
    {
      const IndexVal l(a, aa);
      const Cplx z1 = eltC(U, p1, l);
      U.set(p1, l, conj(z1));
      const Cplx z4 = eltC(U, p4, l);
      U.set(p4, l, conj(z4));
      const Cplx z2 = eltC(U, p2, l);
      const Cplx z3 = eltC(U, p3, l);
      U.set(p2, l, conj(z3));
      U.set(p3, l, conj(z2));
    }
    U.scaleTo(rho.A(i).scale());
  }
  //#pragma omp parallel for
  for (int j = 2; j <= N - 1; ++j)
  {
    ITensor &U = rd.ref(j);
    const Index a = commonIndex(U, rd.A(j + 1));
    const Index b = commonIndex(U, rd.A(j - 1));
    const Index p = siteops(j);
    const IndexVal p1(p, 1), p2(p, 2), p3(p, 3), p4(p, 4);
    for (int aa = 1; aa <= a.dim(); aa++)
    {
      const IndexVal l(a, aa);
      for (int bb = 1; bb <= b.dim(); bb++)
      {
        const IndexVal m(b, bb);
        const Cplx z1 = eltC(U, p1, l, m);
        U.set(p1, l, m, conj(z1));
        const Cplx z4 = eltC(U, p4, l, m);
        U.set(p4, l, m, conj(z4));
        const Cplx z2 = eltC(U, p2, l, m);
        const Cplx z3 = eltC(U, p3, l, m);
        U.set(p2, l, m, conj(z3));
        U.set(p3, l, m, conj(z2));
      }
    }
  }
	rho.plusEq(rd, args);
	rho *= 0.5;
	cout2 << maxLinkDim(rho);
	auto time_end = steady_clock::now();
	auto duration = duration_cast<milliseconds>(time_end - time_step);
	cout2 << ". Duration: " << duration.count() / 1000. << "s" << "\n";
	cout2.flush();
}
