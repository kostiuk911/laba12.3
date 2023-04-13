#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool checkElements(vector<int> L1, vector<int> L2) {
    for (int i = 0; i < L1.size(); i++) {
        if (find(L2.begin(), L2.end(), L1[i]) == L2.end()) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<int> L1 = { 1, 4, 3 };
    vector<int> L2 = { 3, 1, 2, 4 };

    if (checkElements(L1, L2)) {
        cout << "All elements of the L1 list are included in the L2 list" << endl;
    }
    else {
        cout << "Not all elements of the L1 list are included in the L2 list" << endl;
    }

    return 0;
}


