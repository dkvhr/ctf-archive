#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;

    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    int cx = x1, cy = y1;
    int rx = x2, ry = y2;

    int x_dist = abs(rx - cx);
    int y_dist = abs(ry - cy);
    if((x_dist + y_dist)%2)
        cout << "Caring Koala\n";
    else
        cout << "Red Panda\n";

}
