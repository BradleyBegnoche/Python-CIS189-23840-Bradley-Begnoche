# Bradley Begnoche
# 3/26/24
# This program Unit Tests the students file
import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_object_created_required_attributes(self):
        student = Student("Doe", "John", "Computer Science")
        self.assertEqual(student.last_name, "Doe")
        self.assertEqual(student.first_name, "John")
        self.assertEqual(student.major, "Computer Science")
        self.assertEqual(student.gpa, 0.0)

    def test_object_created_all_attributes(self):
        student = Student("Doe", "John", "Computer Science", 3.5)
        self.assertEqual(student.last_name, "Doe")
        self.assertEqual(student.first_name, "John")
        self.assertEqual(student.major, "Computer Science")
        self.assertEqual(student.gpa, 3.5)

    def test_student_str(self):
        student = Student("Doe", "John", "Computer Science", 3.5)
        self.assertEqual(str(student), "Doe, John has major Computer Science with gpa: 3.5")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = Student("", "John", "Computer Science")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = Student("Doe", "", "Computer Science")

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = Student("Doe", "John", "")

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = Student("Doe", "John", "Computer Science", "invalid_gpa")

    def test_object_not_created_error_gpa_out_of_range(self):
        with self.assertRaises(ValueError):
            student = Student("Doe", "John", "Computer Science", 5.0)


if __name__ == '__main__':
    unittest.main()
