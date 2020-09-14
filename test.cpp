#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<vector<int>> A;

    A.push_back({1, 2});
    A.push_back({1, 2});
    A.push_back({1, 2});
    A.push_back({1, 2});

    cout << A.size();
}