class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int fIndex = -1;
        bool first = false;
        int sIndex = -1;
        for(int i = 0; i < nums.size(); i++){
            bool found = nums[i] == target;
            // cout << nums[i] << "  " << fIndex << "  " << sIndex << "  " <<  first << "  " << endl; 
            if(!first && found){
                fIndex = i;
                first = true;
            }
            
            if(first && found){
                sIndex = i;
            }
        
            
        }
        vector<int> res({fIndex, sIndex});
        return res;
        
    }
};