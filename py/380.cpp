// https://www.cnblogs.com/grandyang/p/5740864.html
// 主要技巧:
// 用hash判断这个数字是不是已经有过了.
// 如果要删除, 假设是暴力删除, 那要拿掉要删除的那一个元素, 然后把后面的元素全部挪到前面去.
// 所以复杂度基本上就是O(n)了.
// 所以, 将要删除的元素跟数组最后一个元素调换位置, 然后切掉尾巴, 才能在O(1)时间删掉一个元素.

class RandomizedSet {
public:
    RandomizedSet() {}
    bool insert(int val) {
        if (m.count(val)) return false;
        nums.push_back(val);
        m[val] = nums.size() - 1;
        return true;
    }
    bool remove(int val) {
        if (!m.count(val)) return false;
        int last = nums.back();
        m[last] = m[val];
        nums[m[val]] = last;
        nums.pop_back();
        m.erase(val);
        return true;
    }
    int getRandom() {
        return nums[rand() % nums.size()];
    }
private:
    vector<int> nums;
    unordered_map<int, int> m;
};