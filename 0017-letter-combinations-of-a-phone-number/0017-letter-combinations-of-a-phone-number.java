class Solution {
    
    String[] keyMapping = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    
    public void comboRecursive(String digits, String asf, List<String> ans){
        
        if(digits.length()==0){
            ans.add(asf);
            return;
        }
        char firstDigit = digits.charAt(0);
        String digitLeft = digits.substring(1);
        
        String key = keyMapping[Integer.parseInt(""+firstDigit)];
        for(char ch : key.toCharArray()){
            comboRecursive(digitLeft,""+asf+ch,ans);
        }
        
    }
    
    public List<String> letterCombinations(String digits) {
       
        List<String> ans = new ArrayList<>();
         if(digits.equals("")) return ans;
        
        comboRecursive(digits,"",ans);
        return ans;
        
    }
}