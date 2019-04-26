from codes.common.sort.quick_sort import quick_sort

# Test Purpose:
input1 = [1, 3, 2, 5, 6, 6, 4, 9, 4, 8]
output1 = [1, 2, 3, 4, 4, 5, 6, 6, 8, 9]


class TestQuickSort(object):
    def setup_class(self):
        self.test_mapping = {
            '1': (input1, output1)
        }

    def test_quick_sort(self):
        for key, value in self.test_mapping.items():
            print(f'== Start {key} test ==')
            assert quick_sort(value[0]) == value[1]



