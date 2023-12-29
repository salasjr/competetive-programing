class Solution {
    public String sortSentence(String s) {
        String[] arr = s.split(" ");
        Arrays.sort(arr, new Comparator<String>() {
           public int compare(String s1, String s2) {
               int ch1 = s1.charAt(s1.length()-1);
               int ch2 = s2.charAt(s2.length()-1);
               if(ch1 <= ch2) {
                   return -1;
               } else return 1;
           } 
        });
        StringBuilder str = new StringBuilder();
        for(String st : arr) {
            String temp = st.substring(0, st.length()-1);
            str.append(temp + " ");
        }
        return str.toString().trim();
    }
}