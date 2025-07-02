#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'caesarCipher' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. INTEGER k
 */

string caesarCipher(string s, int k)
{

  // make an alphabet
  // rotate it by k amount
  // map old alphabet to new

  int lc_offset = 97;
  int caps_offset = 65;

  std::map<int, int> rotated;
  for (int i = 0; i <= 25; i++)
  {

    int newVal = (i + k) % 26 + lc_offset;
    rotated[i + lc_offset] = newVal;

    int newVal2 = (i + k) % 26 + caps_offset;
    rotated[i + caps_offset] = newVal2;
  }

  // for(auto [key, val] : rotated){
  //     cout << key << " " << val << endl;
  // }

  string newstring = s;

  for (auto i = 0; i < s.size(); i++)
  {
    // get its ascii value
    int ascii = (int)s[i]; // casting this character to int gets its ascii val

    // if it exists in our map, replace it in the newstring
    if (rotated.count(ascii) > 0)
    {
      // cout << "found value " << s[i] << endl;
      int newAscii = rotated[ascii];
      newstring[i] = (char)newAscii;
    }
  }
  return newstring;
}

int main()
{
  ofstream fout(getenv("OUTPUT_PATH"));

  string n_temp;
  getline(cin, n_temp);

  int n = stoi(ltrim(rtrim(n_temp)));

  string s;
  getline(cin, s);

  string k_temp;
  getline(cin, k_temp);

  int k = stoi(ltrim(rtrim(k_temp)));

  string result = caesarCipher(s, k);

  fout << result << "\n";

  fout.close();

  return 0;
}

string ltrim(const string &str)
{
  string s(str);

  s.erase(
      s.begin(),
      find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

  return s;
}

string rtrim(const string &str)
{
  string s(str);

  s.erase(
      find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
      s.end());

  return s;
}
