import java.util.*;

class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        Map<String, List<Character>> map = new HashMap<>();
        for (String s : allowed) {
            String key = s.substring(0, 2);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s.charAt(2));
        }
        return dfs(bottom, map);
    }

    private boolean dfs(String row, Map<String, List<Character>> map) {
        if (row.length() == 1) return true;
        List<String> nextRows = new ArrayList<>();
        buildNextRows(row, 0, new StringBuilder(), map, nextRows);
        for (String next : nextRows) {
            if (dfs(next, map)) return true;
        }
        return false;
    }

    private void buildNextRows(String row, int index, StringBuilder sb,
                               Map<String, List<Character>> map,
                               List<String> result) {
        if (index == row.length() - 1) {
            result.add(sb.toString());
            return;
        }
        String key = row.substring(index, index + 2);
        if (!map.containsKey(key)) return;
        for (char c : map.get(key)) {
            sb.append(c);
            buildNextRows(row, index + 1, sb, map, result);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
