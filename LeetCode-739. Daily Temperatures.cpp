
class Solution {
public:
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        stack<int> stk;
        vector<int> ans;
        int n = temperatures.size() - 1;
        for (int i = n; i >= 0;i--)
        {
            if(stk.empty())
            {
                stk.push(i); //pushing the index
                ans.push_back(0);
            }
            else
            {

                // if we see that the current element in the stack is smaller than we pop the elements indeces

                while(!stk.empty() && temperatures[stk.top()]<=temperatures[i])
                {
                    stk.pop();
                }
                if(stk.empty())
                {
                    stk.push(i);
                    ans.push_back(0);
                }
                else
                {
                    ans.push_back(stk.top() - i);
                    stk.push(i);
                }
            }

        }

        // as we have answers in reverse order

        reverse(ans.begin(), ans.end());
        return ans;
    }
};
