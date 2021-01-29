#include <string>
#include <iostream>
#include <vector>
#include<iomanip>
using namespace std;
int** getArray(int rows=10);
void swap(int &a,int &b);
int main()
{
    string s1;
    string s2(s1);
    string s3 = s1;
    string s4("value");
    string s5 = "value";
    string s6(5, 'c');
    const char *str = s5.c_str();
    vector<int> v;
    for (int i = 0; i <= 10; i++)
    {
        v.push_back(i);
    }
    for (vector<int>::iterator iter = v.begin(); iter != v.end(); iter++)
    {
        cout << *iter << " ";
    }
    cout << endl<< *str << endl;
    int **arr = getArray();
    for (int i = 0; i < 10; i++)
    {
        delete []arr[i];
    }
    delete []arr;
    int a = 1;
    int b = 10;
    swap(a,b);
    cout<<a<<endl<<b<<endl;
    system("pause");
}

void swap(int &a,int &b)
{
    int c =a;
    a = b;
    b = c;
}

/*
*
*生成二位数组，默认10行
*/
int** getArray(int row)
{
    int **arr = new int *[10];
    for (int i = 0; i < 10; i++)
    {
        /* code */
        arr[i] = new int[i + 1]();
    }
    for (int i = 0; i < 10; i++)
    {
        /* code */
        for (int j = 0; j < i + 1; j++)
        {
            *(arr[i] + j) = i + j;
            cout << *(arr[i] + j) <<setw(3);
        }
        cout << endl;
    }
    return arr;
}