import time


def waiter():
    cook('1 Pasta', 5)
    cook('2 Caesar Salad', 3)
    cook('3 Lamb Chops', 9)


def cook(order, time_to_prepare):
    print(f'{order} getting order.')
    time.sleep(time_to_prepare)
    print(order, 'ready')


if __name__ == '__main__':
    waiter()
