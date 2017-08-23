public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int i=0;i<nums.length; i++) {
            hm.put(nums[i], nums[i]);
        }
        List<Integer>l = new ArrayList<Integer>();
        for (int i=1; i<=nums.length; i++) {
            if (!hm.containsKey(i)){
                l.add(i);
            }
        }
        return l;
    }
}
