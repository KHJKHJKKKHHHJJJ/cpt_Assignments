from collections import deque

def solution(prices):
    results = deque(prices)
    count = 0

    while count < len(prices):
        x = 0

        for price in prices[1:]:
            if results[0] <= price:
                x += 1

        prices.pop(0)
        results.append(x)
        results.popleft()
        
    return results

if __name__ == '__main__':
    prices = [1000,2000,3000,2000,3000]
    print(solution(prices))