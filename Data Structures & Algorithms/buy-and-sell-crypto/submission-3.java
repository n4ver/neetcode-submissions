class Solution {
    public int maxProfit(int[] prices) {
        int minBuy = prices[0];
        int profit = 0;
        for (int sell : prices) {
            profit = Math.max(profit, sell - minBuy);
            if (sell < minBuy) {
                minBuy = sell;
            }
        }
        return profit;
}
}
