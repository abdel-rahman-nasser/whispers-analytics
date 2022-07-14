class FI_Data_Handling:
    def str_num_conv(self, x):
        total = 0
        num_map = {'K': 1000, 'M': 1000000, 'B': 1000000000}
        if x.isdigit():
            total = int(x)
        else:
            if len(x) > 1:
                total = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
        return int(total)
