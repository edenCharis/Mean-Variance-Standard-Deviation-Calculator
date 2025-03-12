import numpy as np

def calculate(list):
     if len(list) == 9:
        array = np.array(list).reshape(3,3)

        mean_axe_0 = array.mean(axis=0)
        mean_axe_1= array.mean(axis=1)
        mean_array = array.mean()

        var_axe_0 = array.var(axis=0)
        var_axe_1= array.var(axis=1)
        var_array = array.var()


        std_axe_0 = array.std(axis=0)
        std_axe_1= array.std(axis=1)
        std_array = array.std()

        min_axe_0 = array.min(axis=0)
        min_axe_1= array.min(axis=1)
        min_array= array.min()

        max_axe_0= array.max(axis=0)
        max_axe_1= array.max(axis=1)
        max_array= array.max()


        sum_axe_0 = array.sum(axis=0)
        sum_axe_1 = array.sum(axis=1)
        sum_array = array.sum()

        calculations = {
            'mean': [mean_axe_0.tolist(), mean_axe_1.tolist(), mean_array],
            'variance': [var_axe_0.tolist(), var_axe_1.tolist(), var_array],
            'standard deviation': [std_axe_0.tolist(), std_axe_1.tolist(), std_array],
            'max': [max_axe_0.tolist(), max_axe_1.tolist(), max_array],
            'min': [min_axe_0.tolist(), min_axe_1.tolist(), min_array],
            'sum': [sum_axe_0.tolist(), sum_axe_1.tolist(), sum_array]
        }
        return calculations
     else:
        raise ValueError("List must contain nine numbers.")
