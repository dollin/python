import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(threadName)s] %(funcName)s:%(lineno)d %(message)s',
)

class Stack:
    stack_items = []

    def push(self, i):
        if len(self.stack_items) == 0:
            self.stack_items.append([i, i])
        else:
            current_min = self.stack_items[-1][1]
            self.stack_items.append([i, i if i < current_min else current_min])

    def pop(self):
        item = self.stack_items[-1]
        self.stack_items.remove(item)
        return item[0]

    def min(self):
        return self.stack_items[-1][1]

if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.push(1)
    logging.info(f"min=1 : {stack.min()}")
    logging.info(f"popped=1 : {stack.pop()}")
    logging.info(f"min=2 : {stack.min()}")
    logging.info(f"popped=3 : {stack.pop()}")
    logging.info(f"min=2 : {stack.min()}")
    logging.info(f"popped=2 : {stack.pop()}")
