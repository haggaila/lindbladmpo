#ifndef _IO_UTILS_
#define _IO_UTILS_
#include "itensor/all.h"
#include <string>
#include <vector>
#include <map>
#include <regex>
using namespace itensor;
using namespace std;
//____________________________________________________________
//The function below translate numbers (etc.) into character strings
//the second parameter (optional) is the precision (digits)

template <class T>
inline string to_string(const T &t, unsigned int precision = 0)
{
  stringstream ss;
  if (precision > 0)
    ss.precision(precision);
  ss << t;
  return ss.str();
}
//____________________________________________________________
template <class T>
ostream &operator<<(ostream &o, const vector<T> &v)
{
  for (unsigned int i = 0; i < v.size(); i++)
    o << "[" << i << "]" << v[i] << " ";
  return o;
}
//____________________________________________________________

inline double char2double(char *a)
{
  char *end_ptr;
  const double x = strtod(a, &end_ptr);
  if (end_ptr == a || ('\0' != *end_ptr))
    cerr << endl
         << "ERROR :" << a
         << " is not a valid format for a double."
         << endl,
        exit(1);
  return x;
}
//____________________________________________________________
vector<string> &split(const string &s, char delimiter,vector<std::string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delimiter)) {
        if (item.length() > 0) {
            elems.push_back(item);
            }
    }
    return elems;
}
vector<string> split(const string &s, char delimiter) {
    vector<string> elems;
    split(s, delimiter, elems);
    return elems;
}
//____________________________________________________________
class Parameters_old : public map<string, double>
{
public:
  double val(string var_name) const
  {
    map<string, double>::const_iterator it = find(var_name);
    if (it == end())
    {
      cerr << "Error: Parameter " << var_name << " is not defined.\n", exit(1);
      return 0;
    }
    else
      return it->second;
  }
  long longval(string var_name) const
  {
    double v = val(var_name);
    if (abs(double(round(v)) - v) < 1e-6)
    {
      return long(round(v));
    }
    else
    {
      cerr << "Error, parameter " << var_name << "=" << v << " is not a long" << endl, exit(1);
      return 0;
    }
  }
  void PRint(ostream &o) const
  {
    for (map<string, double>::const_iterator it = begin(); it != end(); it++)
    {
      o << it->first << "=" << it->second << endl;
    }
  }
  void ReadArguments(int argc, char *argv[])
  {
    for (int n = 1; n < argc; n++)
    {
      string var_name(argv[n]);
      map<string, double>::const_iterator it = find(var_name);

      if (it != end())
      {
        n++;
        if (n == argc)
          cerr << "Error: missing value after " << var_name << endl, exit(1);
        operator[](var_name) = char2double(argv[n]);
      }
      else
      {
        cerr << "Error :" << var_name << endl;
        cout << "List of command-line parameters :\n";
        PRint(cout);
        exit(1);
      }
    }
  }
};
//____________________________________________________________
class Parameters : public map<string, string>
{
public:
  //------------------------------------------------------
  // The method 'ReadFromFile reads an input file (specified by its name) which should be of the following (text) format:
  // variable1 = value_of_variable_1
  // variable2 = value_of_variable_2
  // ...
  //
  // * All spaces are ignored by the parser
  // * Any line without any '=' sign is ignored
  // * All the variables should have been previously declared (see SimulationParameters.h or ModelParameters.h). 
  // At this stage all values are strings, and they are added to the Parameters object.
  // The methods Parameters::val, Parameters::longval, Parameters::boolval, and Parameters::stringval can later be used to retrieve these values as
  // double, long, bool and string.

  void ReadFromFile(string filename)
  {
    ifstream file(filename);
    if (!file) cerr<<"Error: unable to open the file "<<filename<<endl,exit(1);
    else cout<<"Reading parameters from the file "<<filename<<endl;
    string line;
    while (getline(file, line))
    {
      line = regex_replace(line, regex("\\s+"), "");// remove white spaces using a regular expression
      if (line != "")
      {
        string delimiter = "=";
        size_t position = 0;
        string var_name;
        position = line.find(delimiter);
        if (position != string::npos)
        {
          var_name = line.substr(0, position);
          string var_value = line.erase(0, position + delimiter.length());

          map<string, string>::const_iterator it = find(var_name);
          if (it != end())
            operator[](var_name) = var_value;
          else
            cerr << "Error, the input parameter " << var_name << " does not exist in this model.\n", exit(1);
        }
        else
        {
          cout << "Warning: the input line :"
               << line << " has been ignored (no '=')." << endl;
        }
      }
    }
  }
  //------------------------------------------------------
  double val(string var_name) const
  {
    map<string, string>::const_iterator it = find(var_name);
    if (it == end())
    {
      cerr << "Error: Parameter " << var_name << " is not defined.\n", exit(1);
      return 0;
    }
    else
      return stod(it->second);
  }
  //------------------------------------------------------
  long longval(string var_name) const
  {
    map<string, string>::const_iterator it = find(var_name);
    if (it == end())
    {
      cerr << "Error: Parameter " << var_name << " is not defined.\n", exit(1);
      return 0;
    }
    else
    {
      long i;
      try {
          i=stoi(it->second);
        }
        catch(...) {
          cerr<<"Error: was expecting a long int and instead got '"<<it->second<<"'\n",exit(1);
        }
      return i;
    }
  }
  //------------------------------------------------------
  long boolval(string var_name) const
  {
    map<string, string>::const_iterator it = find(var_name);
    if (it == end())
    {
      cerr << "Error: Parameter " << var_name << " is not defined.\n", exit(1);
      return 0;
    }
    else
    {
      string s = it->second;
      if (s == "true")
        return true;
      if (s == "TRUE")
        return true;
      if (s == "1")
        return true;
      if (s == "false")
        return false;
      if (s == "FALSE")
        return false;
      if (s == "0")
        return false;
      cerr << "Error " << var_name << "=" << it->second << " but a boolean was expected: true/false, TRUE/FALSE or or 1/0\n", exit(1);
    }
  } //------------------------------------------------------
  string stringval(string var_name) const
  {
    map<string, string>::const_iterator it = find(var_name);
    if (it == end())
    {
      cerr << "Error: Parameter " << var_name << " is not defined.\n", exit(1);
      return 0;
    }
    else
      return (it->second);
  }
  //------------------------------------------------------
  void PRint(ostream &o) const
  {
    for (map<string, string>::const_iterator it = begin(); it != end(); it++)
    {
      o << it->first << "=" << it->second << endl;
    }
  }
  //------------------------------------------------------
  void ReadArguments(int argc, char *argv[])
  {
    for (int n = 1; n < argc; n++)
    {
      string var_name(argv[n]);
      map<string, string>::const_iterator it = find(var_name);

      if (it != end())
      {
        n++;
        if (n == argc)
          cerr << "Error: missing value after " << var_name << endl, exit(1);
        operator[](var_name) = string(argv[n]);
      }
      else
      {
        cerr << "Error, the input parameter " << var_name << " does not exist in this model.\n";
        cout << "List of command-line parameters :\n";
        PRint(cout);
        exit(1);
      }
    }
  }
  //------------------------------------------------------
  // The method below converts a string of the type 1.2,2,-4.4,3.3 into a vector<double>
  vector<double> doublevec(string var_name) const
  { 
    vector<double> double_vec;
    map<string, string>::const_iterator it = find(var_name);
    if (it == end())
    {
      cerr << "Error: Parameter " << var_name << " is not defined.\n", exit(1);
    }
    else
    {
      vector<string> str_vec;
      cout<<"string V="<<it->second<<endl;
      str_vec=split(it->second, ',');
      for(auto& s: str_vec) {
        double x;
         try {
          x=stod(s);
        }
        catch(...) {
          cerr<<"Error: was expecting a double and instead got "<<s<<endl,exit(1);
        }
        double_vec.push_back(x);
      }
    }
    return double_vec;
  }
  //------------------------------------------------------
  // The method below converts a string of the type 1.2,2,-4.4,3.3 into a vector<double>
  vector<long> longvec(string var_name) const
  { 
    vector<long> long_vec;
    map<string, string>::const_iterator it = find(var_name);
    if (it == end())
    {
      cerr << "Error: Parameter " << var_name << " is not defined.\n", exit(1);
    }
    else
    {
      vector<string> str_vec;
      str_vec=split(it->second, ',');
      for(auto& s: str_vec) {
        long i;
        try {
          i=stoi(s);
        }
        catch(...) {
          cerr<<"Error: was expecting a long int and instead got '"<<s<<"'\n",exit(1);
        }
        long_vec.push_back(i);
      }
    }
    return long_vec;
  }
};
#endif
