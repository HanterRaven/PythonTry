class ConvertCelToFar:
    count = 0

    @staticmethod
    def convert_c_to_f(cel):
        ConvertCelToFar.count += 1
        return 9 / 5 * cel + 32

    @staticmethod
    def convert_f_to_c(far):
        ConvertCelToFar.count += 1
        return 5 / 9 * (far - 32)

    @staticmethod
    def count_of_convert():
        return ConvertCelToFar.count


print(ConvertCelToFar.convert_c_to_f(10))
print(ConvertCelToFar.count_of_convert())
print(ConvertCelToFar.convert_c_to_f(20))
print(ConvertCelToFar.convert_c_to_f(30))
print(ConvertCelToFar.count_of_convert())
print(ConvertCelToFar.convert_f_to_c(50))
print(ConvertCelToFar.convert_f_to_c(68))
print(ConvertCelToFar.convert_f_to_c(86))
print(ConvertCelToFar.count_of_convert())

