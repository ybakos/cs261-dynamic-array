# DO NOT MODIFY THE TESTS IN THIS FILE
# Run me via: python3 -m unittest test_dynamic_array

import unittest
import time
import random
from dynamic_array import DynamicArray


class TestDynamicArray(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A DynamicArray exists.
        """
        try:
            DynamicArray()
        except NameError:
            self.fail("Could not instantiate DynamicArray.")

    # def test_default_initial_capacity(self):
    #     """
    #     The default initial capacity is ten.
    #     """
    #     a = DynamicArray()
    #     self.assertEqual(10, a.capacity)

    # def test_initially_empty(self):
    #     """
    #     A dynamic array is initially empty.
    #     """
    #     a = DynamicArray()
    #     self.assertTrue(a.is_empty())

    # def test_initial_length(self):
    #     """
    #     A dynamic array has an initial length of 0.
    #     """
    #     a = DynamicArray()
    #     self.assertEqual(0, len(a))


    # """
    # Appending and retrieving one value
    # """

    # # Hint: Do the naive thing.
    # def test_append_one_value_to_empty(self):
    #     """
    #     A single value can be appended to and retrieved from a dynamic array.
    #     """
    #     a = DynamicArray()
    #     a.append(42)
    #     self.assertEqual(42, a[0])

    # """
    # Appending and retrieving two values
    # """

    # # Tip: If you haven't gotten this to pass within two minutes, comment it out
    # # and move on.
    # def test_append_two_values(self):
    #     """
    #     Two values can be appended to and retrieved from a dynamic array.
    #     """
    #     a = DynamicArray()
    #     a.append(8)
    #     a.append(6)
    #     self.assertEqual(8, a[0])
    #     self.assertEqual(6, a[1])

    # """
    # Guiding internal data storage, with a static array
    # """

    # def test_data_property(self):
    #     """
    #     Has an internal `data` property that is a numpy ndarray.
    #     """
    #     import numpy as np # Hint: Get an error? Just `pip3 install numpy`
    #     a = DynamicArray()
    #     self.assertEqual(np.ndarray, type(a.data))

    # def test_data_object_references(self):
    #     """
    #     Internal data array stores object references.
    #     """
    #     import numpy as np # Hint: Get an error? Just `pip3 install numpy`
    #     a = DynamicArray()
    #     self.assertEqual('O', a.data.dtype)

    # def test_data_size(self):
    #     """
    #     Length of the data array is the same as the DynamicArray capacity.
    #     """
    #     import numpy as np # Hint: Get an error? Just `pip3 install numpy`
    #     a = DynamicArray()
    #     self.assertEqual(len(a.data), a.capacity)

    # """
    # Guiding appending and retrieving one value.
    # """

    # def test_append_first_value_to_internal_data(self):
    #     """
    #     Appending the first value in an empty DynamicArray puts it in the right
    #     location in the internal data array.
    #     """
    #     a = DynamicArray()
    #     a.append(99)
    #     self.assertEqual(99, a.data[0])

    # def test_retrieve_first_appended_value(self):
    #     """
    #     The first element appended to the DynamicArray is can be retrieved with
    #     index 0.
    #     """
    #     a = DynamicArray()
    #     a.append(100)
    #     self.assertEqual(a[0], a.data[0])
    #     self.assertEqual(100, a[0])

    # """
    # Guiding appending and retrieving two values.
    # """

    # def test_next_index(self):
    #     """
    #     Has a next_index property, which is initially 0.
    #     """
    #     a = DynamicArray()
    #     self.assertEqual(0, a.next_index)

    # def test_next_index(self):
    #     """
    #     After appending the first value, next_index becomes 1.
    #     """
    #     a = DynamicArray()
    #     a.append('FAKE')
    #     self.assertEqual(1, a.next_index)

    # def test_appending_two_values_internal(self):
    #     """
    #     Appending two values stores them in the first and second positions in
    #     the internal data array.
    #     """
    #     a = DynamicArray()
    #     a.append('foo')
    #     a.append('bar')
    #     self.assertEqual('foo', a.data[0])
    #     self.assertEqual('bar', a.data[1])

    # # This is a copy of the same test from way up above. If this passes, uncomment
    # # the other uncommented test. If this is confusing, just ignore this comment.
    # def test_append_two_values_again(self):
    #     """
    #     Two values can be appended to and retrieved from a dynamic array.
    #     """
    #     a = DynamicArray()
    #     a.append(8)
    #     a.append(6)
    #     self.assertEqual(8, a[0])
    #     self.assertEqual(6, a[1])

    # def test_append_four_values(self):
    #     """
    #     Three values can be appended to and retrieved from a dynamic array.
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     a.append('funk')
    #     self.assertEqual('fee', a[0])
    #     self.assertEqual('fi', a[1])
    #     self.assertEqual('fo', a[2])
    #     self.assertEqual('funk', a[3])

    # """
    # Emptiness, len and clearing
    # """

    # def test_is_empty(self):
    #     """
    #     A dynamic array containing data is not empty.
    #     """
    #     a = DynamicArray()
    #     self.assertTrue(a.is_empty())
    #     a.append('FAKE')
    #     self.assertFalse(a.is_empty())

    # def test_clear(self):
    #     """
    #     A cleared dynamic array is empty and has a length of 0.
    #     """
    #     a = DynamicArray()
    #     a.append('FAKE')
    #     a.append('FAKE')
    #     self.assertFalse(a.is_empty())
    #     a.clear()
    #     self.assertTrue(a.is_empty())
    #     self.assertEqual(0, len(a))

    # def test_len(self):
    #     """
    #     The length of a dynamic array is equal to the number of elements appended.
    #     """
    #     a = DynamicArray()
    #     a.append('FAKE')
    #     a.append('FAKE')
    #     self.assertEqual(2, len(a))

    # """
    # Invalid indexes
    # """

    # def test_negative_index(self):
    #     """
    #     Accessing with a negative index raises an IndexError
    #     """
    #     a = DynamicArray()
    #     try:
    #         a[-1]
    #         self.fail("Did not raise IndexError: index out of range.")
    #     except IndexError:
    #         pass

    # def test_large_index(self):
    #     """
    #     Accessing with an index greater than or equal to the last index raises an IndexError
    #     """
    #     a = DynamicArray()
    #     try:
    #         a[0]
    #         self.fail("Did not raise IndexError: index out of range.")
    #     except IndexError:
    #         pass

    # """
    # Removing elements from the end
    # """

    # def test_pop(self):
    #     """
    #     Popping removes and returns the last element
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     last_element = a.pop()
    #     self.assertEqual('fo', last_element)
    #     self.assertEqual(2, len(a))

    # def test_pop_empty(self):
    #     """
    #     Popping from an empty list raises an IndexError: pop from empty array
    #     """
    #     a = DynamicArray()
    #     try:
    #         a.pop()
    #         self.fail("Did not raise IndexError: index out of range.")
    #     except IndexError:
    #         pass

    # """
    # Deleting
    # """

    # def test_delete_last(self):
    #     """
    #     Deleting the last element removes it from the dynamic array.
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     a.delete(2)
    #     self.assertEqual(2, len(a))
    #     self.assertEqual('fi', a.pop())

    # def test_delete_invalid_index(self):
    #     """
    #     Deleting an out of bounds index raises an IndexError: index out of range
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     try:
    #         a.delete(3)
    #         a.delete(-1)
    #         self.fail("Did not raise IndexError: index out of range.")
    #     except IndexError:
    #         pass

    # def test_delete_first(self):
    #     """
    #     Deleting the first element shifts remaining elements to the left.
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     a.delete(0)
    #     self.assertEqual(2, len(a))
    #     self.assertEqual('fi', a[0])
    #     self.assertEqual('fo', a[1])

    # def test_delete_middle(self):
    #     """
    #     Deleting from the middle shifts remaining elements to the left.
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     a.delete(1)
    #     self.assertEqual(2, len(a))
    #     self.assertEqual('fee', a[0])
    #     self.assertEqual('fo', a[1])

    # def test_delete_empty(self):
    #     """
    #     Deleting from an empty array raises an IndexError: index out of range
    #     """
    #     a = DynamicArray()
    #     try:
    #         a.delete(0)
    #         self.fail("Did not raise IndexError: index out of range.")
    #     except IndexError:
    #         pass

    # """
    # Basic insertion
    # """

    # def test_insert_end(self):
    #     """
    #     Inserting after the last element adds the element to the end of the array.
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     a.insert(3, 'funk')
    #     self.assertEqual(4, len(a))
    #     self.assertEqual('fo', a[2])
    #     self.assertEqual('funk', a[3])

    # def test_insert_invalid_index(self):
    #     """
    #     Inserting an out of bounds index raises an IndexError: index out of range.
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     try:
    #         a.insert(4, 'this is more than the next available index')
    #         a.insert(-1, 'this is less than the first index')
    #         self.fail("Did not raise IndexError: index out of range.")
    #     except IndexError:
    #         pass

    # def test_insert_first(self):
    #     """
    #     Inserting a new first element shifts remaining elements to the right.
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     a.insert(0, 'foo')
    #     self.assertEqual(4, len(a))
    #     self.assertEqual('foo', a[0])
    #     self.assertEqual('fee', a[1])
    #     self.assertEqual('fi', a[2])
    #     self.assertEqual('fo', a[3])

    # def test_insert_middle(self):
    #     """
    #     Inserting into the middle shifts elements to the right, to the right.
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     a.append('fo')
    #     a.insert(1, 'foo')
    #     self.assertEqual(4, len(a))
    #     self.assertEqual('fee', a[0])
    #     self.assertEqual('foo', a[1])
    #     self.assertEqual('fi', a[2])
    #     self.assertEqual('fo', a[3])

    # def test_insert_empty(self):
    #     """
    #     Inserting into an empty array at position 0 is ok.
    #     """
    #     a = DynamicArray()
    #     a.insert(0, 'foo')
    #     self.assertEqual(1, len(a))
    #     self.assertEqual('foo', a[0])

    # """
    # Fullness
    # """

    # def test_empty_not_full(self):
    #     """
    #     An empty dynamic array is not full.
    #     """
    #     a = DynamicArray()
    #     self.assertFalse(a.is_full())

    # def test_less_than_capacity(self):
    #     """
    #     A dynamic array with a number of elements less than capacityis not full.
    #     """
    #     a = DynamicArray()
    #     a.append('fee')
    #     a.append('fi')
    #     self.assertTrue(len(a) < a.capacity)
    #     self.assertFalse(a.is_full())

    # def test_full(self):
    #     """
    #     A dynamic array is full when the number of elements fills its internal data array
    #     """
    #     a = DynamicArray()
    #     for _ in range(0, a.capacity):
    #         a.append('fake')
    #     self.assertEqual(10, len(a))
    #     self.assertEqual(10, a.next_index)
    #     self.assertEqual(len(a), a.capacity)
    #     self.assertTrue(a.is_full())

    # """
    # Increasing capacity
    # """

    # def test_append_to_full(self):
    #     """
    #     A full dynamic array expands to accommodate a new appended element.
    #     """
    #     a = DynamicArray()
    #     for _ in range(0, a.capacity):
    #         a.append('fake')
    #     a.append('new value')
    #     self.assertEqual('new value', a[10])

    # def test_new_capacity(self):
    #     """
    #     When expanding, a dynamic array doubles its capacity
    #     """
    #     a = DynamicArray()
    #     for _ in range(0, a.capacity):
    #         a.append('fake')
    #     old_capacity = a.capacity
    #     a.append('new value')
    #     self.assertEqual(2 * old_capacity, a.capacity)

    # def test_insert_to_full(self):
    #     """
    #     A full dynamic array expands to accommodate a new inserted element.
    #     """
    #     a = DynamicArray()
    #     for i in range(0, a.capacity):
    #         a.append(f"fake{i}")
    #     a.insert(0, 'new value')
    #     self.assertEqual('new value', a[0])
    #     self.assertEqual('fake0', a[1])
    #     self.assertEqual('fake9', a[10])


    # """
    # Max, min, and sum
    # """

    # def test_max(self):
    #     """
    #     Max method returns the largest value in the dynamic array.
    #     """
    #     a = DynamicArray()
    #     for _ in range(0, 9):
    #         a.append(random.randint(0, 100))
    #     largest_value = random.randint(101, 150)
    #     a.insert(random.randint(0, 9), largest_value)
    #     self.assertEqual(largest_value, a.max())

    # def test_min(self):
    #     """
    #     Min method returns the smallest value in the dynamic array.
    #     """
    #     a = DynamicArray()
    #     for _ in range(0, 9):
    #         a.append(random.randint(100, 200))
    #     smallest_value = random.randint(0, 50)
    #     a.insert(random.randint(0, 9), smallest_value)
    #     self.assertEqual(smallest_value, a.min())

    # def test_sum(self):
    #     """
    #     Sum method returns the sum of all values in the dynamic array.
    #     """
    #     a = DynamicArray()
    #     for val in range(10, 15):
    #         a.append(val)
    #     self.assertEqual(60, a.sum())

    # def test_max_min_sum_of_empty(self):
    #     """
    #     The max, min or sum of an empty dynamic array is None.
    #     """
    #     a = DynamicArray()
    #     self.assertEqual(None, a.sum())
    #     self.assertEqual(None, a.min())
    #     self.assertEqual(None, a.max())

    # """
    # Search
    # """

    # def test_linear_search(self):
    #     """
    #     The linear search method returns the index of the first occurence of a
    #     value value if it exists in the array, or None if it doesn't.
    #     """
    #     a = DynamicArray()
    #     for i in range(5, 1000005):
    #         a.append(i)
    #     self.assertEqual(None, a.linear_search('LOVE'))
    #     self.assertEqual(0, a.linear_search(5))
    #     start_time = time.time() # Ignore this line, it's just some instrumentation.
    #     self.assertEqual(999999, a.linear_search(1000004))
    #     print(f"\nLinear Search Time: {time.time()-start_time}\n")
    #     random_index = random.randint(0, len(a))
    #     a.insert(random_index, 1)
    #     self.assertEqual(random_index, a.linear_search(1))

    # def test_binary_search(self):
    #     """
    #     The binary search method returns the index of the first occurence of a
    #     value value if it exists in the array, or None if it doesn't.
    #     """
    #     a = DynamicArray()
    #     for i in range(5, 1000005):
    #         a.append(i)
    #     start_time = time.time() # Ignore this line, it's just some instrumentation.
    #     self.assertEqual(999999, a.binary_search(1000004))
    #     print(f"\nBinary Search Time: {time.time()-start_time}\n")


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
