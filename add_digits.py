class add_digits:

    """
    defdef addDigits(self, num: int) -> int:
    def adddigits(self, num):
    """
    def adddigits(self, num):
        if num < 10:
            return num
        while num > 0:
            total = num % 10
            num //= 10
            num += total
            if num < 10:
                return num


def main():
    ad = add_digits()
    print(ad.adddigits(12384))


if __name__ == '__main__':
    main()
