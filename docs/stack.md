# Stack

## 기본적인 컨셉

- LIFO (Last In First Out) 형태의 자료구조
- 삽입 시 걸리는 시간 : O(1)
- 삭제 시 걸리는 시간 : O(1)
- 특정 원소 탐색 시 걸리는 시간 : O(N)

## 파이썬 구현

### 1. 리스트 활용

```python
# initialization
stack = list()
top = 0

# push
stack.append(4)
top += 1

stack.append(9)
top += 1

print(stack)
print(top)

# pop
del stack[top - 1]
print(stack)
```

