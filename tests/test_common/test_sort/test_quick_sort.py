from codes.common.sort.quick_sort import quick_sort

# Test Purpose:
input1 = [2, 3, 1, 5, 2]
output1 = [1, 2, 2, 3, 5]
input2 = [7, 3, 2, 5, 6, 6, 4, 9, 4, 8]
output2 = [2, 3, 4, 4, 5, 6, 6, 7, 8, 9]


class TestQuickSort(object):

    def setup_class(self):
        self.test_mapping = {
            '1': (input1, output1),
            '2': (input2, output2),
        }

    def test_quick_sort(self):
        for key, value in self.test_mapping.items():
            print(f'\n== Start {key} test ==')
            assert quick_sort(value[0]) == value[1]



