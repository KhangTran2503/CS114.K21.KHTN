#include <bits/stdc++.h>
#define ll double
using namespace std;

class Expression_tree
{
    private:
        struct Node
        {
            string key;
            Node *pLeft,*pRight;
            Node()
            {
                key = "";
                pLeft = pRight = NULL;
            }
        };
        stack<string> m_operator;
        stack<Node*> m_node;
        Node* m_root;
    public:
        Expression_tree()
        {
            m_root = NULL;
        }
        Node *NewNode(string key)
        {
            Node *tmp =new Node;
            tmp->key = key;
            tmp->pLeft = NULL;
            tmp->pRight =NULL;
            return tmp;
        }
        void Update_Node()
        {
            Node *tmp = NewNode(m_operator.top());
                m_operator.pop();
            if(!m_node.empty())
            {
                tmp->pRight = m_node.top();
                m_node.pop();
            }
            if(!m_node.empty())
            {
                tmp->pLeft = m_node.top();
                m_node.pop();
            }
            m_node.push(tmp);
        }
        void Operator_Stack(char c)
        {

            if(c == ')')
            {
                while(m_operator.top() != "(")
                    Update_Node();
                if(m_operator.top() == "(")
                    m_operator.pop();
            }else
            {
                string tmp;
                tmp = c;
                m_operator.push(tmp);
            }
        }
        void Insert(string s)
        {
            s = '('+ s + ')';
            int n = s.size();
            int i=0;
            for(i=0; i<n; i++)
            {
                if(s[i] == '(' || s[i] == ')' || s[i] == '+' ||
                   s[i] == '-' || s[i] == '*' || s[i] == '/')
                        Operator_Stack(s[i]);
                if('0'<=s[i] && s[i]<='9')
                {
                    string tmp;
                    tmp = "";
                    while('0'<=s[i] && s[i]<='9')
                        tmp = tmp + s[i++];
                    m_node.push(NewNode(tmp));
                    i--;
                    if(m_operator.top() == "*" || m_operator.top() == "/")
                        Update_Node();
                }
            }
            m_root = m_node.top();
            m_node.pop();
        }
        ll Transform(string tmp)
        {
            ll sum=0;
            for(int i=0;i<tmp.size();i++)
                sum= sum*10 + tmp[i]-'0';
            return sum;
        }
        ll Cal(Node *tmp)
        {
            if(tmp == NULL) return 0;
            if(tmp->key == "*")
                return Cal(tmp->pLeft) * Cal(tmp->pRight);
            if(tmp->key == "/")
                return Cal(tmp->pLeft) / Cal(tmp->pRight);
            if(tmp->key == "-")
                return Cal(tmp->pLeft) - Cal(tmp->pRight);
            if(tmp->key == "+")
                return Cal(tmp->pLeft) + Cal(tmp->pRight);
            return Transform(tmp->key);
        }
        ll Calculate()
        {
            return Cal(m_root);
        }
        void Show(Node *tmp)
        {
            cout << tmp->key <<' ';
        }
        void LNR_Printf(Node *tmp)
        {
            if(tmp == NULL) return;
            LNR_Printf(tmp->pLeft);
            Show(tmp);
            LNR_Printf(tmp->pRight);
        }
        void LNR_Printf()
        {
            LNR_Printf(m_root);
        }
};
typedef Expression_tree ET;
int main()
{
    string s;
    cout << "Nhap bieu thuc: ";
    getline(cin,s);
    ET tree;
    tree.Insert(s);
    tree.LNR_Printf();
    cout<< "\nDap an = " << tree.Calculate();
    return 0;
}
