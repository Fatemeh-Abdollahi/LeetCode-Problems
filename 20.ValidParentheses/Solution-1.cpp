class Solution {
public:
    bool isValid(string s) {
        if(s.size()%2 == 1)
            return false;
        vector <char> c;
        for(int i =0; i < s.size();i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='[')
                c.push_back(s[i]);
            else if(!c.empty()){
                if(s[i]==')' && c.back()=='(')
                    c.pop_back();
                else if(s[i]=='}' && c.back()=='{')
                    c.pop_back();
                else if(s[i]==']' && c.back()=='[')
                    c.pop_back();
                else 
                    return false;
            }
            else return false;
        }
        if(c.empty())
            return true;
        else
            return false;
    }
};